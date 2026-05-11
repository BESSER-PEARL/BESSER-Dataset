





import java.util.List;
import java.util.ArrayList;

public class aml_DiscoveryMethod  {

    private String autoTrigger;
    private String type;
    private String id;
    private String description;
    private String url;
    private String label;
    private String importType;





    private aml_AmlDocument aml_amldocument;


    public aml_DiscoveryMethod(
        String autoTrigger,        String type,        String id,        String description,        String url,        String label,        String importType    ) {
        this.autoTrigger = autoTrigger;
        this.type = type;
        this.id = id;
        this.description = description;
        this.url = url;
        this.label = label;
        this.importType = importType;
    }


    public String getAutotrigger() {
        return autoTrigger;
    }

    public void setAutotrigger(String autoTrigger) {
        this.autoTrigger = autoTrigger;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getImporttype() {
        return importType;
    }

    public void setImporttype(String importType) {
        this.importType = importType;
    }

    public aml_AmlDocument getAml_amldocument() {
        return aml_amldocument;
    }

    public void setAml_amldocument(aml_AmlDocument aml_amldocument) {
        this.aml_amldocument = aml_amldocument;
    }

}