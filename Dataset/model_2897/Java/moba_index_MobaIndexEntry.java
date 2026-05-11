





import java.util.List;
import java.util.ArrayList;

public class moba_index_MobaIndexEntry  {

    private String templateId;
    private String templateDescription;
    private String filename;
    private String templateVersion;
    private String templateName;
    private String relativePath;



    public moba_index_MobaIndexEntry(
        String templateId,        String templateDescription,        String filename,        String templateVersion,        String templateName,        String relativePath    ) {
        this.templateId = templateId;
        this.templateDescription = templateDescription;
        this.filename = filename;
        this.templateVersion = templateVersion;
        this.templateName = templateName;
        this.relativePath = relativePath;
    }


    public String getTemplateid() {
        return templateId;
    }

    public void setTemplateid(String templateId) {
        this.templateId = templateId;
    }
    public String getTemplatedescription() {
        return templateDescription;
    }

    public void setTemplatedescription(String templateDescription) {
        this.templateDescription = templateDescription;
    }
    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }
    public String getTemplateversion() {
        return templateVersion;
    }

    public void setTemplateversion(String templateVersion) {
        this.templateVersion = templateVersion;
    }
    public String getTemplatename() {
        return templateName;
    }

    public void setTemplatename(String templateName) {
        this.templateName = templateName;
    }
    public String getRelativepath() {
        return relativePath;
    }

    public void setRelativepath(String relativePath) {
        this.relativePath = relativePath;
    }


}