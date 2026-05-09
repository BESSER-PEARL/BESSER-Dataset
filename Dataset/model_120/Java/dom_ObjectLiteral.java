





import java.util.List;
import java.util.ArrayList;

public class dom_ObjectLiteral extends Expression {






    private List<dom_PropertyAssignment> dom_propertyassignments;


    public dom_ObjectLiteral(
    ) {
        super(
        );
        this.dom_propertyassignments = new ArrayList<>();
    }

    public dom_ObjectLiteral(
        ArrayList<dom_PropertyAssignment> dom_propertyassignments    ) {
        this.dom_propertyassignments = dom_propertyassignments;
    }


    public List<dom_PropertyAssignment> getDom_propertyassignments() {
        return dom_propertyassignments;
    }

    public void addDom_propertyassignment(Dom_propertyassignment dom_propertyassignment) {
        this.dom_propertyassignments.add(dom_propertyassignment);
    }

}