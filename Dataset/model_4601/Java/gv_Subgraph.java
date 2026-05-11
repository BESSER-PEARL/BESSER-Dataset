





import java.util.List;
import java.util.ArrayList;

public class gv_Subgraph extends Connectable, Commentable, AbstractGraph {

    private String type;



    public gv_Subgraph(
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