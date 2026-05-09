





import java.util.List;
import java.util.ArrayList;

public class RefUML_Element extends EModelElement {






    private List<RefUML_Element> refuml_elements;




    private RefUML_Element refuml_element;




    private List<RefUML_Comment> refuml_comments;




    private RefUML_Relationship refuml_relationship;




    private RefUML_Comment refuml_comment;


    public RefUML_Element(
    ) {
        super(
        );
        this.refuml_elements = new ArrayList<>();
        this.refuml_comments = new ArrayList<>();
    }

    public RefUML_Element(
        ArrayList<RefUML_Element> refuml_elements,        ArrayList<RefUML_Comment> refuml_comments    ) {
        this.refuml_elements = refuml_elements;
        this.refuml_comments = refuml_comments;
    }


    public List<RefUML_Element> getRefuml_elements() {
        return refuml_elements;
    }

    public void addRefuml_element(Refuml_element refuml_element) {
        this.refuml_elements.add(refuml_element);
    }
    public RefUML_Element getRefuml_element() {
        return refuml_element;
    }

    public void setRefuml_element(RefUML_Element refuml_element) {
        this.refuml_element = refuml_element;
    }
    public List<RefUML_Comment> getRefuml_comments() {
        return refuml_comments;
    }

    public void addRefuml_comment(Refuml_comment refuml_comment) {
        this.refuml_comments.add(refuml_comment);
    }
    public RefUML_Relationship getRefuml_relationship() {
        return refuml_relationship;
    }

    public void setRefuml_relationship(RefUML_Relationship refuml_relationship) {
        this.refuml_relationship = refuml_relationship;
    }
    public RefUML_Comment getRefuml_comment() {
        return refuml_comment;
    }

    public void setRefuml_comment(RefUML_Comment refuml_comment) {
        this.refuml_comment = refuml_comment;
    }

}