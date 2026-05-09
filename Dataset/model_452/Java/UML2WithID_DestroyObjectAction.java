





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_DestroyObjectAction extends Action {

    private boolean isDestroyOwnedObjects;
    private boolean isDestroyLinks;



    public UML2WithID_DestroyObjectAction(
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


}