<!-- markdownlint-disable MD033 -->
<!-- This allows HTML <br /> for explicit line breaks. -->
# dcat(1)

<br />

## NAME

`dcat` - Print out a non-VSAM dataset.

<br />

## SYNOPSIS

```text
dcat [-bdhjJlv] DATASET

-b
    Print out dataset contents in "binary mode".

-d
    Print out debug messages.

-h
    Display syntax help.

-j
    Print output in JSON format.
    Options -b (binary mode) and -l (newline suppression) are ignored,
    and do not affect JSON output. Each record is followed by a line break.

    Output appears in this form:
        { "data": { "content": "..." }, "records":<records printed>,
        "content_length":<characters read from the dataset> }

-J
    Prints JSON output in a readable format.
    This option forces -j if it was not set.

-l
    Suppresses printing of newline characters between dataset records.

-v
    Print out verbose command information.
```

<br />

## DESCRIPTION

`dcat` prints out an entire non-VSAM dataset.  It can be either a
partitioned dataset member or a sequential dataset.

`dcat` can print active generation datasets referenced by absolute or relative
names.

If the input dataset contains NULL characters (0x00), they are converted to
spaces when printed. Other unprintable characters are converted to spaces
if the -b argument is not specified.

<br />

## EXAMPLES

Print the content of a sequential dataset:

```sh
dcat "IBMUSER.DATASET.ABC"
```

<br />
<br />

Print the content of a PDS member into a file:

```sh
dcat "IBMUSER.DATASET.PDS(MEMBER1)" >> sample.txt
```

<br />
<br />

Print in a readable JSON format:

```sh
dcat -J 'IBMUSER.MY.TEXT'

Output:
{
    "data": {
            "content": "Record 1
            Record 2
            "
    },
    "records": 2,
    "content_length": 162
}
```

<br />
<br />

## EXIT VALUES

```text
0
    dcat completed successfully.

non-zero
    dcat failed. See error messages for details.
```

<br />

## SEE ALSO

[dhead(1)](dhead.md), [decho(1)](decho.md), [dtail(1)](dtail.md)
