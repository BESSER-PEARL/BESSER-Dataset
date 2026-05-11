





import java.util.List;
import java.util.ArrayList;

public class gaml_Statement  {

    private String key;
    private String firstFacet;





    private gaml_Expression gaml_expression;




    private gaml_Block gaml_block;




    private gaml_Block gaml_block;




    private List<gaml_Facet> gaml_facets;


    public gaml_Statement(
        String key,        String firstFacet    ) {
        this.key = key;
        this.firstFacet = firstFacet;
        this.gaml_facets = new ArrayList<>();
    }

    public gaml_Statement(
        String key,        String firstFacet        ArrayList<gaml_Facet> gaml_facets    ) {
        this.key = key;
        this.firstFacet = firstFacet;
        this.gaml_facets = gaml_facets;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getFirstfacet() {
        return firstFacet;
    }

    public void setFirstfacet(String firstFacet) {
        this.firstFacet = firstFacet;
    }

    public gaml_Expression getGaml_expression() {
        return gaml_expression;
    }

    public void setGaml_expression(gaml_Expression gaml_expression) {
        this.gaml_expression = gaml_expression;
    }
    public gaml_Block getGaml_block() {
        return gaml_block;
    }

    public void setGaml_block(gaml_Block gaml_block) {
        this.gaml_block = gaml_block;
    }
    public gaml_Block getGaml_block() {
        return gaml_block;
    }

    public void setGaml_block(gaml_Block gaml_block) {
        this.gaml_block = gaml_block;
    }
    public List<gaml_Facet> getGaml_facets() {
        return gaml_facets;
    }

    public void addGaml_facet(Gaml_facet gaml_facet) {
        this.gaml_facets.add(gaml_facet);
    }

}