from abaqusConstants import *
from .LoadState import LoadState


class BodyHeatFluxState(LoadState):
    """The BodyHeatFluxState object stores the propagating data for a Body BodyHeatFlux object
    in a step. One instance of this object is created internally by the BodyHeatFlux object
    for each step. The instance is also deleted internally by the BodyHeatFlux object.
    The BodyHeatFluxState object has no constructor or methods.
    The BodyHeatFluxState object is derived from the LoadState object.

    Attributes
    ----------
    magnitude: float
        A Float specifying the Body heat flux magnitude.
    magnitudeState: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the Body heat flux magnitude.
        Possible values are UNSET, SET, UNCHANGED, and MODIFIED.
    amplitudeState: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.
    status: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the :py:class:`~abaqus.Load.LoadState.LoadState` object. Possible
        values are:
            - NOT_YET_ACTIVE
            - CREATED
            - PROPAGATED
            - MODIFIED
            - DEACTIVATED
            - NO_LONGER_ACTIVE
            - TYPE_NOT_APPLICABLE
            - INSTANCE_NOT_APPLICABLE
            - BUILT_INTO_BASE_STATE
    amplitude: str
        A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].steps[name].loadStates[name]

    The corresponding analysis keywords are:

    - DFLUX
    """

    # A Float specifying the Body heat flux magnitude.
    magnitude: float = None

    # A SymbolicConstant specifying the propagation state of the Body heat flux magnitude.
    # Possible values are UNSET, SET, UNCHANGED, and MODIFIED.
    magnitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    # values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the LoadState object. Possible
    # values are:
    # - NOT_YET_ACTIVE
    # - CREATED
    # - PROPAGATED
    # - MODIFIED
    # - DEACTIVATED
    # - NO_LONGER_ACTIVE
    # - TYPE_NOT_APPLICABLE
    # - INSTANCE_NOT_APPLICABLE
    # - BUILT_INTO_BASE_STATE
    status: SymbolicConstant = None

    # A String specifying the name of the amplitude reference. The String is empty if the load
    # has no amplitude reference.
    amplitude: str = ""
