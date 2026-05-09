





import java.util.List;
import java.util.ArrayList;

public class UMLModel_DestroyObjectAction extends Action {

    private String isDestroyOwnedObjects;
    private String isDestroyLinks;



    public UMLModel_DestroyObjectAction(
        String isDestroyOwnedObjects,        String isDestroyLinks    ) {
        super(
        );
        this.isDestroyOwnedObjects = isDestroyOwnedObjects;
        this.isDestroyLinks = isDestroyLinks;
    }


    public String getIsdestroyownedobjects() {
        return isDestroyOwnedObjects;
    }

    public void setIsdestroyownedobjects(String isDestroyOwnedObjects) {
        this.isDestroyOwnedObjects = isDestroyOwnedObjects;
    }
    public String getIsdestroylinks() {
        return isDestroyLinks;
    }

    public void setIsdestroylinks(String isDestroyLinks) {
        this.isDestroyLinks = isDestroyLinks;
    }


}