





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlModel  {

    private String baseUri;
    private String alias;
    private String version;





    private List<sADL_SadlAnnotation> sadl_sadlannotations;




    private sADL_SadlImport sadl_sadlimport;




    private List<sADL_SadlModelElement> sadl_sadlmodelelements;




    private List<sADL_SadlImport> sadl_sadlimports;


    public sADL_SadlModel(
        String baseUri,        String alias,        String version    ) {
        this.baseUri = baseUri;
        this.alias = alias;
        this.version = version;
        this.sadl_sadlannotations = new ArrayList<>();
        this.sadl_sadlmodelelements = new ArrayList<>();
        this.sadl_sadlimports = new ArrayList<>();
    }

    public sADL_SadlModel(
        String baseUri,        String alias,        String version        ArrayList<sADL_SadlAnnotation> sadl_sadlannotations,        ArrayList<sADL_SadlModelElement> sadl_sadlmodelelements,        ArrayList<sADL_SadlImport> sadl_sadlimports    ) {
        this.baseUri = baseUri;
        this.alias = alias;
        this.version = version;
        this.sadl_sadlannotations = sadl_sadlannotations;
        this.sadl_sadlmodelelements = sadl_sadlmodelelements;
        this.sadl_sadlimports = sadl_sadlimports;
    }

    public String getBaseuri() {
        return baseUri;
    }

    public void setBaseuri(String baseUri) {
        this.baseUri = baseUri;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public List<sADL_SadlAnnotation> getSadl_sadlannotations() {
        return sadl_sadlannotations;
    }

    public void addSadl_sadlannotation(Sadl_sadlannotation sadl_sadlannotation) {
        this.sadl_sadlannotations.add(sadl_sadlannotation);
    }
    public sADL_SadlImport getSadl_sadlimport() {
        return sadl_sadlimport;
    }

    public void setSadl_sadlimport(sADL_SadlImport sadl_sadlimport) {
        this.sadl_sadlimport = sadl_sadlimport;
    }
    public List<sADL_SadlModelElement> getSadl_sadlmodelelements() {
        return sadl_sadlmodelelements;
    }

    public void addSadl_sadlmodelelement(Sadl_sadlmodelelement sadl_sadlmodelelement) {
        this.sadl_sadlmodelelements.add(sadl_sadlmodelelement);
    }
    public List<sADL_SadlImport> getSadl_sadlimports() {
        return sadl_sadlimports;
    }

    public void addSadl_sadlimport(Sadl_sadlimport sadl_sadlimport) {
        this.sadl_sadlimports.add(sadl_sadlimport);
    }

}