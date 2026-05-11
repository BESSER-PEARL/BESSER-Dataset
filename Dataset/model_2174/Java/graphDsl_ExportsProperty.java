





import java.util.List;
import java.util.ArrayList;

public class graphDsl_ExportsProperty  {






    private List<graphDsl_ExportsVariable> graphdsl_exportsvariables;




    private graphDsl_OptionalProperty graphdsl_optionalproperty;




    private graphDsl_FacetProperty graphdsl_facetproperty;


    public graphDsl_ExportsProperty(
    ) {
        this.graphdsl_exportsvariables = new ArrayList<>();
    }

    public graphDsl_ExportsProperty(
        ArrayList<graphDsl_ExportsVariable> graphdsl_exportsvariables    ) {
        this.graphdsl_exportsvariables = graphdsl_exportsvariables;
    }


    public List<graphDsl_ExportsVariable> getGraphdsl_exportsvariables() {
        return graphdsl_exportsvariables;
    }

    public void addGraphdsl_exportsvariable(Graphdsl_exportsvariable graphdsl_exportsvariable) {
        this.graphdsl_exportsvariables.add(graphdsl_exportsvariable);
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