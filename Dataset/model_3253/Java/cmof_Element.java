





import java.util.List;
import java.util.ArrayList;

public class cmof_Element  {






    private List<cmof_Comment> cmof_comments;




    private cmof_Element cmof_element;




    private cmof_Comment cmof_comment;




    private cmof_Relationship cmof_relationship;




    private cmof_Constraint cmof_constraint;




    private List<cmof_Element> cmof_elements;




    private cmof_Tag cmof_tag;


    public cmof_Element(
    ) {
        this.cmof_comments = new ArrayList<>();
        this.cmof_elements = new ArrayList<>();
    }

    public cmof_Element(
        ArrayList<cmof_Comment> cmof_comments,        ArrayList<cmof_Element> cmof_elements    ) {
        this.cmof_comments = cmof_comments;
        this.cmof_elements = cmof_elements;
    }


    public List<cmof_Comment> getCmof_comments() {
        return cmof_comments;
    }

    public void addCmof_comment(Cmof_comment cmof_comment) {
        this.cmof_comments.add(cmof_comment);
    }
    public cmof_Element getCmof_element() {
        return cmof_element;
    }

    public void setCmof_element(cmof_Element cmof_element) {
        this.cmof_element = cmof_element;
    }
    public cmof_Comment getCmof_comment() {
        return cmof_comment;
    }

    public void setCmof_comment(cmof_Comment cmof_comment) {
        this.cmof_comment = cmof_comment;
    }
    public cmof_Relationship getCmof_relationship() {
        return cmof_relationship;
    }

    public void setCmof_relationship(cmof_Relationship cmof_relationship) {
        this.cmof_relationship = cmof_relationship;
    }
    public cmof_Constraint getCmof_constraint() {
        return cmof_constraint;
    }

    public void setCmof_constraint(cmof_Constraint cmof_constraint) {
        this.cmof_constraint = cmof_constraint;
    }
    public List<cmof_Element> getCmof_elements() {
        return cmof_elements;
    }

    public void addCmof_element(Cmof_element cmof_element) {
        this.cmof_elements.add(cmof_element);
    }
    public cmof_Tag getCmof_tag() {
        return cmof_tag;
    }

    public void setCmof_tag(cmof_Tag cmof_tag) {
        this.cmof_tag = cmof_tag;
    }

}