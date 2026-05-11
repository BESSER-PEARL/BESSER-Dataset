





import java.util.List;
import java.util.ArrayList;

public class graphDsl_ChildrenProperty  {

    private String name;





    private graphDsl_OptionalProperty graphdsl_optionalproperty;




    private graphDsl_FacetProperty graphdsl_facetproperty;


    public graphDsl_ChildrenProperty(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graphDsl_OptionalProperty getGraphdsl_optionalproperty() {
        return graphdsl_optionalproperty;
    }

    public void setGraphdsl_optionalproperty(graphDsl_OptionalProperty graphdsl_optionalproperty) {
        this.graphdsl_optionalproperty = graphdsl_optionalproperty;
    }
    public graphDsl_FacetProperty getGraphdsl_facetproperty() {
        return graphdsl_facetproperty;
    }

    public void setGraphdsl_facetproperty(graphDsl_FacetProperty graphdsl_facetproperty) {
        this.graphdsl_facetproperty = graphdsl_facetproperty;
    }

}