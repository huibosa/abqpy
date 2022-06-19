from abaqusConstants import *
from .InteractionState import InteractionState


class AcousticImpedanceState(InteractionState):
    """The AcousticImpedanceState object stores the propagating data of an AcousticImpedance
    object in a step. One instance of this object is created internally by the
    AcousticImpedance object for each step. The instance is also deleted internally by the
    AcousticImpedance object.
    The AcousticImpedanceState object has no constructor or methods.
    The AcousticImpedanceState object is derived from the InteractionState object.

    Attributes
    ----------
    interactionPropertyState: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the **interactionProperty** member.
        Possible values are UNSET, SET, UNCHANGED, and FREED.
    interactionProperty: str
        A String specifying the name of the :py:class:`~abaqus.Interaction.AcousticImpedanceProp.AcousticImpedanceProp` object associated with this
        interaction.
    status: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the :py:class:`~abaqus.Interaction.InteractionState.InteractionState` object.
        Possible values are:
            - NOT_YET_ACTIVE
            - CREATED
            - PROPAGATED
            - MODIFIED
            - DEACTIVATED
            - NO_LONGER_ACTIVE
            - TYPE_NOT_APPLICABLE
            - INSTANCE_NOT_APPLICABLE
            - BUILT_INTO_BASE_STATE

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].steps[name].interactionStates[name]

    The corresponding analysis keywords are:

    - SIMPEDANCE
    """

    # A SymbolicConstant specifying the propagation state of the **interactionProperty** member.
    # Possible values are UNSET, SET, UNCHANGED, and FREED.
    interactionPropertyState: SymbolicConstant = None

    # A String specifying the name of the AcousticImpedanceProp object associated with this
    # interaction.
    interactionProperty: str = ""

    # A SymbolicConstant specifying the propagation state of the InteractionState object.
    # Possible values are:
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
