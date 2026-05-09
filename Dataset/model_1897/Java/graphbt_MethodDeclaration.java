





import java.util.List;
import java.util.ArrayList;

public class graphbt_MethodDeclaration  {

    private String name;
    private String type;





    private graphbt_Library graphbt_library;


    public graphbt_MethodDeclaration(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public graphbt_Library getGraphbt_library() {
        return graphbt_library;
    }

    public void setGraphbt_library(graphbt_Library graphbt_library) {
        this.graphbt_library = graphbt_library;
    }

}