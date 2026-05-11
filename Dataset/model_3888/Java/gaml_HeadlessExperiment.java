





import java.util.List;
import java.util.ArrayList;

public class gaml_HeadlessExperiment  {

    private String key;
    private String importURI;
    private String firstFacet;
    private String name;





    private gaml_ExperimentFileStructure gaml_experimentfilestructure;


    public gaml_HeadlessExperiment(
        String key,        String importURI,        String firstFacet,        String name    ) {
        this.key = key;
        this.importURI = importURI;
        this.firstFacet = firstFacet;
        this.name = name;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
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

}