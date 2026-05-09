





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_DestroyObjectAction extends Action {

    private String isDestroyLinks;
    private String isDestroyOwnedObjects;



    public uml3_0_0_DestroyObjectAction(
        String isDestroyLinks,        String isDestroyOwnedObjects    ) {
        super(
        );
        this.isDestroyLinks = isDestroyLinks;
        this.isDestroyOwnedObjects = isDestroyOwnedObjects;
    }


    public String getIsdestroylinks() {
        return isDestroyLinks;
    }

    public void setIsdestroylinks(String isDestroyLinks) {
        this.isDestroyLinks = isDestroyLinks;
    }
    public String getIsdestroyownedobjects() {
        return isDestroyOwnedObjects;
    }

    public void setIsdestroyownedobjects(String isDestroyOwnedObjects) {
        this.isDestroyOwnedObjects = isDestroyOwnedObjects;
    }


}