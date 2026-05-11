





import java.util.List;
import java.util.ArrayList;

public class Graphql_Schema  {

    private String name;





    private List<Graphql_Type> graphql_types;


    public Graphql_Schema(
        String name    ) {
        this.name = name;
        this.graphql_types = new ArrayList<>();
    }

    public Graphql_Schema(
        String name        ArrayList<Graphql_Type> graphql_types    ) {
        this.name = name;
        this.graphql_types = graphql_types;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Graphql_Type> getGraphql_types() {
        return graphql_types;
    }

    public void addGraphql_type(Graphql_type graphql_type) {
        this.graphql_types.add(graphql_type);
    }

}