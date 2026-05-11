





import java.util.List;
import java.util.ArrayList;

public class gaml_HeadlessExperiment  {

    private String importURI;
    private String key;
    private String firstFacet;
    private String name;





    private gaml_ExperimentFileStructure gaml_experimentfilestructure;




    private List<gaml_Facet> gaml_facets;




    private gaml_Block gaml_block;


    public gaml_HeadlessExperiment(
        String importURI,        String key,        String firstFacet,        String name    ) {
        this.importURI = importURI;
        this.key = key;
        this.firstFacet = firstFacet;
        this.name = name;
        this.gaml_facets = new ArrayList<>();
    }

    public gaml_HeadlessExperiment(
        String importURI,        String key,        String firstFacet,        String name        ArrayList<gaml_Facet> gaml_facets    ) {
        this.importURI = importURI;
        this.key = key;
        this.firstFacet = firstFacet;
        this.name = name;
        this.gaml_facets = gaml_facets;
    }

    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gaml_ExperimentFileStructure getGaml_experimentfilestructure() {
        return gaml_experimentfilestructure;
    }

    public void setGaml_experimentfilestructure(gaml_ExperimentFileStructure gaml_experimentfilestructure) {
        this.gaml_experimentfilestructure = gaml_experimentfilestructure;
    }
    public List<gaml_Facet> getGaml_facets() {
        return gaml_facets;
    }

    public void addGaml_facet(Gaml_facet gaml_facet) {
        this.gaml_facets.add(gaml_facet);
    }
    public gaml_Block getGaml_block() {
        return gaml_block;
    }

    public void setGaml_block(gaml_Block gaml_block) {
        this.gaml_block = gaml_block;
    }

}