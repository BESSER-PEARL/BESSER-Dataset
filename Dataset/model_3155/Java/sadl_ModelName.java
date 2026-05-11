





import java.util.List;
import java.util.ArrayList;

public class sadl_ModelName  {

    private String version;
    private String baseUri;
    private String alias;
    private String annType;





    private sadl_Model sadl_model;


    public sadl_ModelName(
        String version,        String baseUri,        String alias,        String annType    ) {
        this.version = version;
        this.baseUri = baseUri;
        this.alias = alias;
        this.annType = annType;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
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
    public String getAnntype() {
        return annType;
    }

    public void setAnntype(String annType) {
        this.annType = annType;
    }

    public sadl_Model getSadl_model() {
        return sadl_model;
    }

    public void setSadl_model(sadl_Model sadl_model) {
        this.sadl_model = sadl_model;
    }

}