





import java.util.List;
import java.util.ArrayList;

public class statemachine_Named  {

    private String comment;
    private String name;



    public statemachine_Named(
        String comment,        String name    ) {
        this.comment = comment;
        this.name = name;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}