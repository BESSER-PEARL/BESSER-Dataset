





import java.util.List;
import java.util.ArrayList;

public class graphDsl_Facet  {

    private String name;





    private graphDsl_ComponentOrFacet graphdsl_componentorfacet;


    public graphDsl_Facet(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graphDsl_ComponentOrFacet getGraphdsl_componentorfacet() {
        return graphdsl_componentorfacet;
    }

    public void setGraphdsl_componentorfacet(graphDsl_ComponentOrFacet graphdsl_componentorfacet) {
        this.graphdsl_componentorfacet = graphdsl_componentorfacet;
    }

}