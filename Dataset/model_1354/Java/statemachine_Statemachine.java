





import java.util.List;
import java.util.ArrayList;

public class statemachine_Statemachine extends Named {

    private String associatedTree;
    private String associatedAttribute;



    public statemachine_Statemachine(
        String associatedTree,        String associatedAttribute    ) {
        super(
        );
        this.associatedTree = associatedTree;
        this.associatedAttribute = associatedAttribute;
    }


    public String getAssociatedtree() {
        return associatedTree;
    }

    public void setAssociatedtree(String associatedTree) {
        this.associatedTree = associatedTree;
    }
    public String getAssociatedattribute() {
        return associatedAttribute;
    }

    public void setAssociatedattribute(String associatedAttribute) {
        this.associatedAttribute = associatedAttribute;
    }


}