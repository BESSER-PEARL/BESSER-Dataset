





import java.util.List;
import java.util.ArrayList;

public class GraphML_Element extends LocatedElement {

    private String id;



    public GraphML_Element(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}