<!-- markdownlint-disable MD033 -->
<!-- This allows HTML <br /> for explicit line breaks. -->
# ddiff(1)

<br />

## NAME

`ddiff` - Compare two datasets (partitioned and sequential) matching one or more patterns.

<br />

### SYNOPSIS

```text
ddiff [-dhiv] [-Q<tmphlq>] [-c<cols>] [-C<num>] [<dataset-pattern1>] [<dataset-pattern2>]

-c
    specify column comparison specifiers to pass to SUPERCE.

-C
    display <num> lines of context around a displayed line.

-d
    Print out debug messages.

-h
    Display syntax help.

-i
    Ignore case

-Q
    Use an alternative high-level qualifier (HLQ) for temporary dataset name.
    This will override the TMPHLQ environment variable.

-v
    Print out verbose command information.
```

<br />

## ENVIRONMENT VARIABLES

```text
TMPHLQ
    overrides the current high-level qualifier used for temporary dataset name.
```

<br />

## DESCRIPTION

Compare two datasets to each other. The datasets can be specified using
standard wildcards and may be sequential, partitioned, or partitioned dataset
members.

`ddiff` supports generation dataset relative name notation when the name is
fully specified with no wildcard characters.

The `-C` and `-i` options behave in a consistent manner with `diff`.

<br />

## EXAMPLES

Compare 2 text files from columns 1 to 72

```sh
ddiff -c1:72 tstradm.data1.txt tstradm.data2.txt
```

<br />
<br />

## EXIT VALUES

```text
0
    No differences between the files compared.

1
    ddiff compared the files and found them to be different.
```
