# core/formatter.py
from colorama import Fore, Style


def format_primary_key(res: dict) -> None:
    """
    Format output for primary key uniqueness check.
    Prints number of PK violations if available.
    """
    cnt = res.get("pk_violation_cnt")
    if cnt is not None:
        print(f"             ↪ pk_violation_cnt: {cnt}")


def format_nulls(res: dict) -> None:
    """
    Format output for null value check.
    Prints column name and number of nulls.
    """
    for item in res.get("columns_with_null", []):
        print(f"             ↪ {item['column']}: {item['nulls']} nulls")


def format_basic_stats(res: dict) -> None:
    """
    Format output for basic table stats check.
    Prints row count and column count.
    """
    row_count = res.get("row_count")
    column_count = res.get("column_count")
    if row_count is not None:
        print(f"             ↪ row_count: {row_count}")
    if column_count is not None:
        print(f"             ↪ column_count: {column_count}")


def format_error(res: dict) -> None:
    """
    Format output for checks that resulted in an error.
    Prints the error message.
    """
    print(f"             ↪ error: {res.get('error', '')}")


def format_skipped(res: dict) -> None:
    """
    Format output for skipped checks.
    Prints the reason the check was skipped.
    """
    print(f"             ↪ reason: {res.get('reason', '')}")


def format_nothing(res: dict) -> None:
    """
    Default formatter for checks with no additional output.
    Does nothing.
    """
    pass


FORMATTER_MAP = {
    "null_value_check": format_nulls,
    "null_value_check_view": format_nulls,
    "basic_stats": format_basic_stats,
    "primary_key_uniqueness": format_primary_key,
    "foreign_key_check": format_nothing,
    "value_range_check": format_nothing,
    "SKIPPED": format_skipped,
    "ERROR": format_error,
}


class ResultFormatter:
    """
    Formats and prints QA check results in a human-readable summary.
    Selects an appropriate formatter based on the check type or status.
    """

    def print_summary(self, results: list[dict]) -> None:
        """
        Prints a formatted summary for a list of QA check results.

        Parameters:
            results (list[dict]): A list of QA check result dictionaries.
        """
        for res in results:
            check = res.get("check", "N/A")
            status = res.get("status", "UNKNOWN")

            symbol = {
                "PASS": "✅",
                "FAIL": "❌",
                "ERROR": "⚠️",
                "HAS_NULLS": "ℹ️",
                "NO_NULLS": "👍",
                "SKIPPED": "⏭️",
                "INFO": "ℹ️",
            }.get(status, "")

            # Color-coded status tag
            color_status = {
                "PASS": Fore.GREEN,
                "FAIL": Fore.RED,
                "ERROR": Fore.RED,
                "SKIPPED": Fore.YELLOW,
                "HAS_NULLS": Fore.YELLOW,
                "NO_NULLS": Fore.GREEN,
                "INFO": Fore.CYAN,
            }.get(status, Style.RESET_ALL)

            print(f"{color_status}[{status:<10}]  {check:<25} {symbol}{Style.RESET_ALL}")

            # Select formatter based on check or fallback to status
            formatter = FORMATTER_MAP.get(check) or FORMATTER_MAP.get(status, format_nothing)
            formatter(res)
