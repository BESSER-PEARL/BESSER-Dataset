





import java.util.List;
import java.util.ArrayList;

public class graphpattern_Profile  {

    private String name;
    private String description;
    private String id;





    private graphpattern_Bundle graphpattern_bundle;


    public graphpattern_Profile(
        String name,        String description,        String id    ) {
        this.name = name;
        this.description = description;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public graphpattern_Bundle getGraphpattern_bundle() {
        return graphpattern_bundle;
    }

    public void setGraphpattern_bundle(graphpattern_Bundle graphpattern_bundle) {
        this.graphpattern_bundle = graphpattern_bundle;
    }

}