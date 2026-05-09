





import java.util.List;
import java.util.ArrayList;

public class GraphML_Port extends LocatedElement {

    private String name;



    public GraphML_Port(
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


}