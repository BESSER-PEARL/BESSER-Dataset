





import java.util.List;
import java.util.ArrayList;

public class statemachine_Named  {

    private String name;
    private String comment;



    public statemachine_Named(
        String name,        String comment    ) {
        this.name = name;
        this.comment = comment;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}