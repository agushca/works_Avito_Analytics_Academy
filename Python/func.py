import csv


def get_csv_agg_stats(
        filepath: str = "C:/Users/user/Downloads/Corp_Summary.csv",
        sep: str = ";",
        encoding: str = "utf-8",
        groupby_col: int = 0,
        agg_col: int = 1,
        header: bool = True,
        keep_duplicates: bool = True
):
    """
    Extract aggregated statistics from a CSV file and return them as a dictionary.
    Keyword arguments:
        filepath (str, optional) -- The path to the CSV file (default 'data/Corp_Summary.csv').
        sep (str, optional) -- The separator used in the CSV file (default ';').
        encoding (str, optional) -- The encoding of the CSV file (default 'utf-8').
        groupby_col (int, optional) -- The column index to group by (default 0).
        agg_col (int, optional) -- The column index to aggregate (default 1).
        header (bool, optional) -- Whether the CSV file has a header row (default True).

    """
    stats = {}
    with open(filepath, encoding=encoding) as f:
        csv_reader = csv.reader(f)
        next(csv_reader) if header else None
        for row in csv_reader:
            row_parts = row[0].split(sep)
            if row_parts[groupby_col] in stats:
                if keep_duplicates:
                    stats[row_parts[groupby_col]].append(row_parts[agg_col])
                elif row_parts[agg_col] not in stats[row_parts[groupby_col]]:
                    stats[row_parts[groupby_col]].append(row_parts[agg_col])
            else:
                stats[row_parts[groupby_col]] = [row_parts[agg_col]]
    return stats

def print_deptments_hierarchy(deptments_hierarchy: dict) -> None:
    """
    Print department-teams hierarchy from a department-teams hierarchy dictionary.
    Keyword arguments:
        deptments_hierarchy (dict) -- A dictionary representing the department-teams hierarchy.

    """
    print("_________Department structure___________")
    for dept in deptments_hierarchy:
        print(f"Department - {dept}")
        for dept_team in deptments_hierarchy[dept]:
            print(f" • {dept_team}")
    print("_________________________________________")


def print_deptments_slry_stats(deptments_slry_stats: dict) -> None:
    """
    Print salary statistics for each department from a salary statistics for each department dict.
    Keyword arguments:
        deptments_slry_stats (dict) -- A dictionary representing the salary statistics for each department.

    """
    print("_______Salary statistics by department________")
    for dept in deptments_slry_stats:
        deptments_slry_aggregated = [int(sal) for sal in deptments_slry_stats[dept]]
        print(
            f"{dept}\n"
            f" • MIN SALARY = {min(deptments_slry_aggregated)}\n"
            f" • MAX SALARY = {max(deptments_slry_aggregated)}\n"
            f" • AVG SALARY = {sum(deptments_slry_aggregated) / len(deptments_slry_aggregated)}"
        )
    print("_____________________________________________")





def save_slry_stats(
        slry_stats: dict,
        output_filepath="data/output_detartment_statistics.csv"
) -> None:
    """
    Third option in menu;
    Save department salary statistics to a CSV file.
    Keyword arguments:
        slry_stats (dict) -- A dictionary with the salary statistics for each department;
        output_filepath (str, optional) -- A path to the final CSV file.

    """
    with open(output_filepath, "w", newline="", encoding="UTF-8") as output:
        fld_names = ["Department", "MAX SALARY", "MIN SALARY", "AVG SALARY"]
        writer = csv.DictWriter(output, fieldnames=fld_names)
        writer.writeheader()

        for dept, salaries in slry_stats.items():
            dept_sal_arr = [int(sal) for sal in salaries]
            writer.writerow({
                "Department - ": dept,
                "• MIN SALARY": min(dept_sal_arr),
                "• MAX SALARY": max(dept_sal_arr),
                "• AVG SALARY": sum(dept_sal_arr) / len(dept_sal_arr)
            })


if __name__ == "__main__":
    print("\nHey there!👋\n")
    while True:
        print(
            "Select an option:\n"
            "1 - Show departsment's hierarchy\n"
            "2 - Show department's summary report\n"
            "3 - Save summary report to CSV file\n"
            "4 - Exit"
        )
        choice = input("Write the action number: ")

        if choice == "1":
            deptments_hierarchy = get_csv_agg_stats(groupby_col=1, agg_col=2, keep_duplicates=False)
            print_deptments_hierarchy(deptments_hierarchy)
        elif choice == "2":
            deptments_slry_stats = get_csv_agg_stats(groupby_col=1, agg_col=5)
            print_deptments_slry_stats(deptments_slry_stats)
        elif choice == "3":
            slry_stats = get_csv_agg_stats(groupby_col=1, agg_col=5)
            save_slry_stats(slry_stats)
            print("Summary report successfully saved to a CSV file.")
        elif choice == "4":
            print("See you!")
            break
        else:
            print("Incorrect. You should choose a number (1-4)")
