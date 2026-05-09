





import java.util.List;
import java.util.ArrayList;

public class uml_Element  {






    private uml_Comment uml_comment;




    private List<uml_Comment> uml_comments;




    private uml_Element uml_element;




    private uml_Element uml_element;




    private uml_Relationship uml_relationship;


    public uml_Element(
    ) {
        this.uml_comments = new ArrayList<>();
    }

    public uml_Element(
        ArrayList<uml_Comment> uml_comments    ) {
        this.uml_comments = uml_comments;
    }


    public uml_Comment getUml_comment() {
        return uml_comment;
    }

    public void setUml_comment(uml_Comment uml_comment) {
        this.uml_comment = uml_comment;
    }
    public List<uml_Comment> getUml_comments() {
        return uml_comments;
    }

    public void addUml_comment(Uml_comment uml_comment) {
        this.uml_comments.add(uml_comment);
    }
    public uml_Element getUml_element() {
        return uml_element;
    }

    public void setUml_element(uml_Element uml_element) {
        this.uml_element = uml_element;
    }
    public uml_Element getUml_element() {
        return uml_element;
    }

    public void setUml_element(uml_Element uml_element) {
        this.uml_element = uml_element;
    }
    public uml_Relationship getUml_relationship() {
        return uml_relationship;
    }

    public void setUml_relationship(uml_Relationship uml_relationship) {
        this.uml_relationship = uml_relationship;
    }

}