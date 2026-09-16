"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""
# ^ entire docstring copied exactly from mp1-part1.md's "Starter Code" section

import argparse                           # from Starter Code imports in mp1-part1.md
import logging                            # from Starter Code imports in mp1-part1.md
import sys                                # from Starter Code imports in mp1-part1.md
from pathlib import Path                  # from Starter Code imports in mp1-part1.md


logger = logging.getLogger(__name__)      # from Starter Code in mp1-part1.md, copied exactly


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    # function name, parameter, and docstring copied exactly from Starter Code in mp1-part1.md
    logging.basicConfig(
        # logging.basicConfig(...) call pattern from class2.md's "Basic Logging Example"
        # and repeated in class2_with_solution.md's Solution section
        level=logging.DEBUG if verbose else logging.INFO,
        # satisfies mp1-part1.md requirement #1: "Use logging.DEBUG when verbose is True.
        # Use logging.INFO when verbose is False."
        format="%(asctime)s %(levelname)-8s %(message)s",
        # exact format string from class2.md's Basic Logging Example / class2_with_solution.md Solution
        # satisfies mp1-part1.md requirement #1: "Include the time, log level, and message"
        datefmt="%H:%M:%S"
        # exact datefmt string from class2.md's Basic Logging Example / class2_with_solution.md Solution
    )


def parse_arguments():
    """Parse command-line arguments."""
    # function name and docstring copied exactly from Starter Code in mp1-part1.md
    parser = argparse.ArgumentParser(
        description="Process a data file through the pipeline."
        # styled after class2_with_solution.md Solution's
        # ArgumentParser(description="Check the quality of a CSV file.")
    )

    parser.add_argument(
        "--input", "-i",
        # long/short form from mp1-part1.md's "2. parse_arguments()" table: --input, -i
        required=True,
        # satisfies mp1-part1.md requirement: "--input and --output must be required"
        help="Path to the input file"
        # styled after class2_with_solution.md Solution's help="CSV file to check"
    )

    parser.add_argument(
        "--output", "-o",
        # long/short form from mp1-part1.md's "2. parse_arguments()" table: --output, -o
        required=True,
        # satisfies mp1-part1.md requirement: "--input and --output must be required"
        help="Path to the output file"
        # styled after class2_with_solution.md Solution's help text pattern
    )

    parser.add_argument(
        "--format",
        # long form only, no short form listed in mp1-part1.md's table
        choices=["csv", "json"],
        # satisfies mp1-part1.md requirement: "--format must accept only csv or json"
        default="csv",
        # satisfies mp1-part1.md requirement: "The default output format must be csv"
        help="Output format: csv or json (default: csv)"
        # written to describe the choices/default per mp1-part1.md's table description
    )

    parser.add_argument(
        "--verbose", "-v",
        # long/short form from mp1-part1.md's "2. parse_arguments()" table: --verbose, -v
        action="store_true",
        # same action="store_true" pattern used in class2.md and class2_with_solution.md
        help="Enable verbose (DEBUG) logging"
        # satisfies mp1-part1.md requirement: "--verbose / -v should enable verbose logging"
    )

    return parser.parse_args()
    # satisfies mp1-part1.md requirement: "The function should return the parsed arguments"
    # same parser.parse_args() call used in class2.md and class2_with_solution.md


def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    # function name, parameter, and docstring copied exactly from Starter Code in mp1-part1.md
    p = Path(filepath)
    # from mp1-part1.md's "3. validate_input(filepath)" section: "Use pathlib: Path(filepath).is_file()"
    # variable name "p" styled after class2_with_solution.md Solution's "p = Path(args.input)"
    if not p.is_file():
        # if/else shape styled after class2_with_solution.md Solution's
        # "if not p.is_file(): ... else: ..." file-check block
        logger.error(f"Input file not found: {filepath}")
        # satisfies mp1-part1.md requirement: "Log an ERROR message... if the path is not a valid file"
        # message wording matches mp1-part1.md's example: "Input file not found: fake.csv"
        return False
        # satisfies mp1-part1.md requirement: "Return... False if the path is not a valid file"
    else:
        logger.info(f"Input file validated: {filepath}")
        # satisfies mp1-part1.md requirement: "Log an INFO message when the input file is successfully validated"
        # message wording matches mp1-part1.md's example: "Input file validated: data/sales.csv"
        return True
        # satisfies mp1-part1.md requirement: "Return True if the input path is a valid file"


def main():
    """Main pipeline function."""
    # function name and docstring copied exactly from Starter Code in mp1-part1.md
    args = parse_arguments()
    # satisfies mp1-part1.md "4. main()" Step 1: "Parse the command-line arguments"

    setup_logging(args.verbose)
    # satisfies mp1-part1.md "4. main()" Step 2: "Set up logging using the --verbose option"

    logger.debug(f"Arguments parsed: input={args.input}, output={args.output}, format={args.format}")
    # satisfies mp1-part1.md "4. main()" Step 3: "Log the parsed arguments at the DEBUG level"
    # message wording matches mp1-part1.md's "Example Output" section

    if not validate_input(args.input):
        # satisfies mp1-part1.md "4. main()" Step 4: "Validate the input file"
        sys.exit(1)
        # satisfies mp1-part1.md "4. main()" Step 5: "Exit with status code 1 if the input file is invalid"


if __name__ == "__main__":
    main()
# ^ this bottom block copied exactly from mp1-part1.md's "Starter Code" section