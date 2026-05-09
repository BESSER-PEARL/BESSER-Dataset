





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Element extends EModelElement {






    private RefOntoUML_Relationship refontouml_relationship;




    private RefOntoUML_Comment refontouml_comment;




    private RefOntoUML_Element refontouml_element;




    private List<RefOntoUML_Comment> refontouml_comments;




    private RefOntoUML_Element refontouml_element;


    public RefOntoUML_Element(
    ) {
        super(
        );
        this.refontouml_comments = new ArrayList<>();
    }

    public RefOntoUML_Element(
        ArrayList<RefOntoUML_Comment> refontouml_comments    ) {
        this.refontouml_comments = refontouml_comments;
    }


    public RefOntoUML_Relationship getRefontouml_relationship() {
        return refontouml_relationship;
    }

    public void setRefontouml_relationship(RefOntoUML_Relationship refontouml_relationship) {
        this.refontouml_relationship = refontouml_relationship;
    }
    public RefOntoUML_Comment getRefontouml_comment() {
        return refontouml_comment;
    }

    public void setRefontouml_comment(RefOntoUML_Comment refontouml_comment) {
        this.refontouml_comment = refontouml_comment;
    }
    public RefOntoUML_Element getRefontouml_element() {
        return refontouml_element;
    }

    public void setRefontouml_element(RefOntoUML_Element refontouml_element) {
        this.refontouml_element = refontouml_element;
    }
    public List<RefOntoUML_Comment> getRefontouml_comments() {
        return refontouml_comments;
    }

    public void addRefontouml_comment(Refontouml_comment refontouml_comment) {
        this.refontouml_comments.add(refontouml_comment);
    }
    public RefOntoUML_Element getRefontouml_element() {
        return refontouml_element;
    }

    public void setRefontouml_element(RefOntoUML_Element refontouml_element) {
        this.refontouml_element = refontouml_element;
    }

}