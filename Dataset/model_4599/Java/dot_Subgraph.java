





import java.util.List;
import java.util.ArrayList;

public class dot_Subgraph extends Commentable, Connectable, AbstractGraph {

    private String type;



    public dot_Subgraph(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}