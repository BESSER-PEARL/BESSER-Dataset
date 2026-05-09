





import java.util.List;
import java.util.ArrayList;

public class petrinet_metamodel_Element  {

    private String comments;
    private String name;



    public petrinet_metamodel_Element(
        String comments,        String name    ) {
        this.comments = comments;
        this.name = name;
    }


    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}