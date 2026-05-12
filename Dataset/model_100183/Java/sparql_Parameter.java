





import java.util.List;
import java.util.ArrayList;

public class sparql_Parameter extends GraphNode {

    private String name;



    public sparql_Parameter(
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