





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Element extends EModelElement {






    private List<uml3_0_0_Comment> uml3_0_0_comments;




    private uml3_0_0_Comment uml3_0_0_comment;




    private List<uml3_0_0_Element> uml3_0_0_elements;




    private uml3_0_0_Element uml3_0_0_element;




    private uml3_0_0_Relationship uml3_0_0_relationship;


    public uml3_0_0_Element(
    ) {
        super(
        );
        this.uml3_0_0_comments = new ArrayList<>();
        this.uml3_0_0_elements = new ArrayList<>();
    }

    public uml3_0_0_Element(
        ArrayList<uml3_0_0_Comment> uml3_0_0_comments,        ArrayList<uml3_0_0_Element> uml3_0_0_elements    ) {
        this.uml3_0_0_comments = uml3_0_0_comments;
        this.uml3_0_0_elements = uml3_0_0_elements;
    }


    public List<uml3_0_0_Comment> getUml3_0_0_comments() {
        return uml3_0_0_comments;
    }

    public void addUml3_0_0_comment(Uml3_0_0_comment uml3_0_0_comment) {
        this.uml3_0_0_comments.add(uml3_0_0_comment);
    }
    public uml3_0_0_Comment getUml3_0_0_comment() {
        return uml3_0_0_comment;
    }

    public void setUml3_0_0_comment(uml3_0_0_Comment uml3_0_0_comment) {
        this.uml3_0_0_comment = uml3_0_0_comment;
    }
    public List<uml3_0_0_Element> getUml3_0_0_elements() {
        return uml3_0_0_elements;
    }

    public void addUml3_0_0_element(Uml3_0_0_element uml3_0_0_element) {
        this.uml3_0_0_elements.add(uml3_0_0_element);
    }
    public uml3_0_0_Element getUml3_0_0_element() {
        return uml3_0_0_element;
    }

    public void setUml3_0_0_element(uml3_0_0_Element uml3_0_0_element) {
        this.uml3_0_0_element = uml3_0_0_element;
    }
    public uml3_0_0_Relationship getUml3_0_0_relationship() {
        return uml3_0_0_relationship;
    }

    public void setUml3_0_0_relationship(uml3_0_0_Relationship uml3_0_0_relationship) {
        this.uml3_0_0_relationship = uml3_0_0_relationship;
    }

}