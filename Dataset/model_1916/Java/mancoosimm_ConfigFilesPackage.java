





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_ConfigFilesPackage extends Package {

    private String maintainer;
    private String priority;
    private String description;
    private String uploaders;
    private String section;
    private String checkSum;
    private String tag;





    private mancoosimm_Configuration mancoosimm_configuration;


    public mancoosimm_ConfigFilesPackage(
        String maintainer,        String priority,        String description,        String uploaders,        String section,        String checkSum,        String tag    ) {
        super(
        );
        this.maintainer = maintainer;
        this.priority = priority;
        this.description = description;
        this.uploaders = uploaders;
        this.section = section;
        this.checkSum = checkSum;
        this.tag = tag;
    }


    public String getMaintainer() {
        return maintainer;
    }

    public void setMaintainer(String maintainer) {
        this.maintainer = maintainer;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getUploaders() {
        return uploaders;
    }

    public void setUploaders(String uploaders) {
        this.uploaders = uploaders;
    }
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }
    public String getChecksum() {
        return checkSum;
    }

    public void setChecksum(String checkSum) {
        this.checkSum = checkSum;
    }
    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }

    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }

}