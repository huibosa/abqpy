from abaqusConstants import *


class AnimationController:
    """The AnimationController object controls all object-based animation to be displayed in
    the viewports. The AnimationController object has no constructor. Abaqus creates the
    **animationController** member when it creates the Session object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import animation
            session.viewports[name].animationController
    """

    #: A SymbolicConstant specifying the type of movie to play. Possible values are
    #: SCALE_FACTOR, HARMONIC, TIME_HISTORY, and NONE. The default value is NONE.
    animationType: SymbolicConstant = NONE

    #: A SymbolicConstant specifying the state of the animation controller. Possible values are
    #: STOP and PLAY. The default value is STOP.
    state: SymbolicConstant = STOP

    def play(self, duration: SymbolicConstant = UNLIMITED):
        """This method begins the animation.

        Parameters
        ----------
        duration
            The SymbolicConstant UNLIMITED or an Int specifying how many seconds to play the
            animation. The default value is UNLIMITED.

        Raises
        ------
        AnimationError: animationType not set
            If **animationType** = NONE:
        """
        ...

    def stop(self):
        """This method stops the animation."""
        ...

    def incrementFrame(self):
        """This method increments the animation frame."""
        ...

    def decrementFrame(self):
        """This method decrements the animation frame."""
        ...

    def showFrame(self, frame: int = None, value: float = None):
        """This method renders the specified frame of the animation.

        Parameters
        ----------
        frame
            An Int specifying the frame number.
        value
            A Float specifying the frame: for **animationType** = TIME_HISTORY the frame with the time
            nearest to this value, for **animationType** = HARMONIC the frame with the angle nearest to
            this value, for **animationType** = SCALE_FACTOR the frame with the scale value nearest to
            this value.
        """
        ...

    def showFirstFrame(self):
        """This method renders the first frame of the animation."""
        ...

    def showLastFrame(self):
        """This method renders the last frame of the animation."""
        ...

    def setValues(self, animationType: SymbolicConstant = NONE):
        """This method modifies the AnimationController object.

        Parameters
        ----------
        animationType
            A SymbolicConstant specifying the type of movie to play. Possible values are
            SCALE_FACTOR, HARMONIC, TIME_HISTORY, and NONE. The default value is NONE.

        Raises
        ------
        RangeError
        """
        ...
