





import java.util.List;
import java.util.ArrayList;

public class sparql_BlankNode extends GraphNode {

    private String name;



    public sparql_BlankNode(
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