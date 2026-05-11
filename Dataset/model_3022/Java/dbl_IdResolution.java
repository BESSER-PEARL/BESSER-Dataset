





import java.util.List;
import java.util.ArrayList;

public class dbl_IdResolution  {

    private String metaModelPlatformURI;





    private List<dbl_Pattern> dbl_patterns;




    private dbl_Module dbl_module;


    public dbl_IdResolution(
        String metaModelPlatformURI    ) {
        this.metaModelPlatformURI = metaModelPlatformURI;
        this.dbl_patterns = new ArrayList<>();
    }

    public dbl_IdResolution(
        String metaModelPlatformURI        ArrayList<dbl_Pattern> dbl_patterns    ) {
        this.metaModelPlatformURI = metaModelPlatformURI;
        this.dbl_patterns = dbl_patterns;
    }

    public String getMetamodelplatformuri() {
        return metaModelPlatformURI;
    }

    public void setMetamodelplatformuri(String metaModelPlatformURI) {
        this.metaModelPlatformURI = metaModelPlatformURI;
    }

    public List<dbl_Pattern> getDbl_patterns() {
        return dbl_patterns;
    }

    public void addDbl_pattern(Dbl_pattern dbl_pattern) {
        this.dbl_patterns.add(dbl_pattern);
    }
    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }

}