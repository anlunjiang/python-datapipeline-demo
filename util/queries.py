from itertools import chain

import pandas as pd
from sqlalchemy.orm import Session


def query_to_dataframe(*qs, session: Session = None):
    """
    Executes one or more given "Query" objects and returns the results in the form of
    a "DataFrame". All queries are assumed to return the same columns. The column names
    are taken from "qs[0].column_descriptions" and will take into account any applied
    column labels. If "session" is given, "with_session" will be called on each given
    Query before retrieving the data.

    Args:
        *qs: SqlAlchemy Query Object
        session: Optional Session
    Returns:
        df: DataFrame
    """
    column_names = [c["name"] for c in qs[0].column_descriptions]

    if session is not None:
        qs = (q.with_session(session) for q in qs)

    query_results = chain.from_iterable(q.all() for q in qs)

    return pd.DataFrame(query_results, columns=column_names)
