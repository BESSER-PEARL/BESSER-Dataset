





import java.util.List;
import java.util.ArrayList;

public class behavior_Element  {






    private behavior_Comment behavior_comment;




    private List<behavior_Element> behavior_elements;




    private List<behavior_Comment> behavior_comments;




    private behavior_Element behavior_element;


    public behavior_Element(
    ) {
        this.behavior_elements = new ArrayList<>();
        this.behavior_comments = new ArrayList<>();
    }

    public behavior_Element(
        ArrayList<behavior_Element> behavior_elements,        ArrayList<behavior_Comment> behavior_comments    ) {
        this.behavior_elements = behavior_elements;
        this.behavior_comments = behavior_comments;
    }


    public behavior_Comment getBehavior_comment() {
        return behavior_comment;
    }

    public void setBehavior_comment(behavior_Comment behavior_comment) {
        this.behavior_comment = behavior_comment;
    }
    public List<behavior_Element> getBehavior_elements() {
        return behavior_elements;
    }

    public void addBehavior_element(Behavior_element behavior_element) {
        this.behavior_elements.add(behavior_element);
    }
    public List<behavior_Comment> getBehavior_comments() {
        return behavior_comments;
    }

    public void addBehavior_comment(Behavior_comment behavior_comment) {
        this.behavior_comments.add(behavior_comment);
    }
    public behavior_Element getBehavior_element() {
        return behavior_element;
    }

    public void setBehavior_element(behavior_Element behavior_element) {
        this.behavior_element = behavior_element;
    }

}