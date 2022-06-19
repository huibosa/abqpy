from ..Region.Region import Region


class IMARegion:
    """A IMARegion is an object used to define material instance name volume fractions for the
    MaterialAssignment predefined field.

    Attributes
    ----------
    region: Region
        A :py:class:`~abaqus.Region.Region.Region` object specifying the sub-region of the selected part instance to which the
        volume fractions will be applied.
    fractionList: float
        A tuple of Floats specifying the volume fractions, per material instance name. The
        length of the tuple corresponds to the number of material instance names, as established
        by the assigned Eulerian section.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].predefinedFields[name].assignmentList
    """

    # A Region object specifying the sub-region of the selected part instance to which the
    # volume fractions will be applied.
    region: Region = Region()

    # A tuple of Floats specifying the volume fractions, per material instance name. The
    # length of the tuple corresponds to the number of material instance names, as established
    # by the assigned Eulerian section.
    fractionList: float = None
