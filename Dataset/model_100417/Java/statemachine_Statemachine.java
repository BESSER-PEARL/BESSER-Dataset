





import java.util.List;
import java.util.ArrayList;

public class statemachine_Statemachine extends Named {

    private String associatedAttribute;
    private String associatedTree;



    public statemachine_Statemachine(
        String associatedAttribute,        String associatedTree    ) {
        super(
        );
        this.associatedAttribute = associatedAttribute;
        this.associatedTree = associatedTree;
    }


    public String getAssociatedattribute() {
        return associatedAttribute;
    }

    public void setAssociatedattribute(String associatedAttribute) {
        this.associatedAttribute = associatedAttribute;
    }
    public String getAssociatedtree() {
        return associatedTree;
    }

    public void setAssociatedtree(String associatedTree) {
        this.associatedTree = associatedTree;
    }


}