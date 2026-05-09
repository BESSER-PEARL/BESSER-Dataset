





import java.util.List;
import java.util.ArrayList;

public class UML2_DestroyObjectAction extends Action {

    private boolean isDestroyOwnedObjects;
    private boolean isDestroyLinks;





    private UML2_InputPin uml2_inputpin;


    public UML2_DestroyObjectAction(
        boolean isDestroyOwnedObjects,        boolean isDestroyLinks    ) {
        super(
        );
        this.isDestroyOwnedObjects = isDestroyOwnedObjects;
        this.isDestroyLinks = isDestroyLinks;
    }


    public boolean getIsdestroyownedobjects() {
        return isDestroyOwnedObjects;
    }

    public void setIsdestroyownedobjects(boolean isDestroyOwnedObjects) {
        this.isDestroyOwnedObjects = isDestroyOwnedObjects;
    }
    public boolean getIsdestroylinks() {
        return isDestroyLinks;
    }

    public void setIsdestroylinks(boolean isDestroyLinks) {
        this.isDestroyLinks = isDestroyLinks;
    }

    public UML2_InputPin getUml2_inputpin() {
        return uml2_inputpin;
    }

    public void setUml2_inputpin(UML2_InputPin uml2_inputpin) {
        this.uml2_inputpin = uml2_inputpin;
    }

}