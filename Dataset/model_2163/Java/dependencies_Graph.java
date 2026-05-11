





import java.util.List;
import java.util.ArrayList;

public class dependencies_Graph extends NamedElement {

    private String priority;



    public dependencies_Graph(
        String priority    ) {
        super(
        );
        this.priority = priority;
    }


    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }


}