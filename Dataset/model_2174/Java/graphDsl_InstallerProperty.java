





import java.util.List;
import java.util.ArrayList;

public class graphDsl_InstallerProperty  {

    private String name;





    private graphDsl_ComponentProperties graphdsl_componentproperties;


    public graphDsl_InstallerProperty(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graphDsl_ComponentProperties getGraphdsl_componentproperties() {
        return graphdsl_componentproperties;
    }

    public void setGraphdsl_componentproperties(graphDsl_ComponentProperties graphdsl_componentproperties) {
        this.graphdsl_componentproperties = graphdsl_componentproperties;
    }

}