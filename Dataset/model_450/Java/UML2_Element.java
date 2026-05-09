





import java.util.List;
import java.util.ArrayList;

public class UML2_Element  {






    private UML2_Constraint uml2_constraint;




    private UML2_ActivityPartition uml2_activitypartition;




    private List<UML2_Element> uml2_elements;




    private UML2_Element uml2_element;




    private UML2_DirectedRelationship uml2_directedrelationship;




    private UML2_DirectedRelationship uml2_directedrelationship;




    private UML2_Relationship uml2_relationship;


    public UML2_Element(
    ) {
        this.uml2_elements = new ArrayList<>();
    }

    public UML2_Element(
        ArrayList<UML2_Element> uml2_elements    ) {
        this.uml2_elements = uml2_elements;
    }


    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }
    public UML2_ActivityPartition getUml2_activitypartition() {
        return uml2_activitypartition;
    }

    public void setUml2_activitypartition(UML2_ActivityPartition uml2_activitypartition) {
        this.uml2_activitypartition = uml2_activitypartition;
    }
    public List<UML2_Element> getUml2_elements() {
        return uml2_elements;
    }

    public void addUml2_element(Uml2_element uml2_element) {
        this.uml2_elements.add(uml2_element);
    }
    public UML2_Element getUml2_element() {
        return uml2_element;
    }

    public void setUml2_element(UML2_Element uml2_element) {
        this.uml2_element = uml2_element;
    }
    public UML2_DirectedRelationship getUml2_directedrelationship() {
        return uml2_directedrelationship;
    }

    public void setUml2_directedrelationship(UML2_DirectedRelationship uml2_directedrelationship) {
        this.uml2_directedrelationship = uml2_directedrelationship;
    }
    public UML2_DirectedRelationship getUml2_directedrelationship() {
        return uml2_directedrelationship;
    }

    public void setUml2_directedrelationship(UML2_DirectedRelationship uml2_directedrelationship) {
        this.uml2_directedrelationship = uml2_directedrelationship;
    }
    public UML2_Relationship getUml2_relationship() {
        return uml2_relationship;
    }

    public void setUml2_relationship(UML2_Relationship uml2_relationship) {
        this.uml2_relationship = uml2_relationship;
    }

}