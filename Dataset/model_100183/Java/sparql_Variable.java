





import java.util.List;
import java.util.ArrayList;

public class sparql_Variable extends GroupCondition, GraphNode {

    private String name;





    private sparql_SelectQuery sparql_selectquery;


    public sparql_Variable(
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

    public sparql_SelectQuery getSparql_selectquery() {
        return sparql_selectquery;
    }

    public void setSparql_selectquery(sparql_SelectQuery sparql_selectquery) {
        this.sparql_selectquery = sparql_selectquery;
    }

}