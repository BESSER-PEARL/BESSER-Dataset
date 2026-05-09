





import java.util.List;
import java.util.ArrayList;

public class dot_Subgraph extends Statement {

    private String name;





    private dot_EdgeTarget dot_edgetarget;


    public dot_Subgraph(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dot_EdgeTarget getDot_edgetarget() {
        return dot_edgetarget;
    }

    public void setDot_edgetarget(dot_EdgeTarget dot_edgetarget) {
        this.dot_edgetarget = dot_edgetarget;
    }

}