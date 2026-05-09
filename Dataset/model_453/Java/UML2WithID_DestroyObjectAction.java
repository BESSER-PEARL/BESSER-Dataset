





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_DestroyObjectAction extends Action {

    private boolean isDestroyLinks;
    private boolean isDestroyOwnedObjects;





    private UML2WithID_InputPin uml2withid_inputpin;


    public UML2WithID_DestroyObjectAction(
        boolean isDestroyLinks,        boolean isDestroyOwnedObjects    ) {
        super(
        );
        this.isDestroyLinks = isDestroyLinks;
        this.isDestroyOwnedObjects = isDestroyOwnedObjects;
    }


    public boolean getIsdestroylinks() {
        return isDestroyLinks;
    }

    public void setIsdestroylinks(boolean isDestroyLinks) {
        this.isDestroyLinks = isDestroyLinks;
    }
    public boolean getIsdestroyownedobjects() {
        return isDestroyOwnedObjects;
    }

    public void setIsdestroyownedobjects(boolean isDestroyOwnedObjects) {
        this.isDestroyOwnedObjects = isDestroyOwnedObjects;
    }

    public UML2WithID_InputPin getUml2withid_inputpin() {
        return uml2withid_inputpin;
    }

    public void setUml2withid_inputpin(UML2WithID_InputPin uml2withid_inputpin) {
        this.uml2withid_inputpin = uml2withid_inputpin;
    }

}