





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_HalfInstalledReinstRequiredPackage extends Package {

    private String checkSum;
    private String uploaders;
    private String priority;
    private String maintainer;
    private String tag;
    private String description;
    private String section;





    private mancoosimm_Configuration mancoosimm_configuration;


    public mancoosimm_HalfInstalledReinstRequiredPackage(
        String checkSum,        String uploaders,        String priority,        String maintainer,        String tag,        String description,        String section    ) {
        super(
        );
        this.checkSum = checkSum;
        this.uploaders = uploaders;
        this.priority = priority;
        this.maintainer = maintainer;
        this.tag = tag;
        this.description = description;
        this.section = section;
    }


    public String getChecksum() {
        return checkSum;
    }

    public void setChecksum(String checkSum) {
        this.checkSum = checkSum;
    }
    public String getUploaders() {
        return uploaders;
    }

    public void setUploaders(String uploaders) {
        this.uploaders = uploaders;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getMaintainer() {
        return maintainer;
    }

    public void setMaintainer(String maintainer) {
        this.maintainer = maintainer;
    }
    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }

    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }

}