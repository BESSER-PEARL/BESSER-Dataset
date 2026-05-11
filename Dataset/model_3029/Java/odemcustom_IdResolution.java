





import java.util.List;
import java.util.ArrayList;

public class odemcustom_IdResolution  {

    private String metaModelPlatformURI;





    private odemcustom_Module odemcustom_module;




    private List<odemcustom_Pattern> odemcustom_patterns;


    public odemcustom_IdResolution(
        String metaModelPlatformURI    ) {
        this.metaModelPlatformURI = metaModelPlatformURI;
        this.odemcustom_patterns = new ArrayList<>();
    }

    public odemcustom_IdResolution(
        String metaModelPlatformURI        ArrayList<odemcustom_Pattern> odemcustom_patterns    ) {
        this.metaModelPlatformURI = metaModelPlatformURI;
        this.odemcustom_patterns = odemcustom_patterns;
    }

    public String getMetamodelplatformuri() {
        return metaModelPlatformURI;
    }

    public void setMetamodelplatformuri(String metaModelPlatformURI) {
        this.metaModelPlatformURI = metaModelPlatformURI;
    }

    public odemcustom_Module getOdemcustom_module() {
        return odemcustom_module;
    }

    public void setOdemcustom_module(odemcustom_Module odemcustom_module) {
        this.odemcustom_module = odemcustom_module;
    }
    public List<odemcustom_Pattern> getOdemcustom_patterns() {
        return odemcustom_patterns;
    }

    public void addOdemcustom_pattern(Odemcustom_pattern odemcustom_pattern) {
        this.odemcustom_patterns.add(odemcustom_pattern);
    }

}