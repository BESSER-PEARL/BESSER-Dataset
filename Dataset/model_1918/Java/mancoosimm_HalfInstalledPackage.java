





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_HalfInstalledPackage extends Package {

    private String tag;
    private String section;
    private String maintainer;
    private String uploaders;
    private String checkSum;
    private String priority;
    private String description;





    private mancoosimm_Configuration mancoosimm_configuration;


    public mancoosimm_HalfInstalledPackage(
        String tag,        String section,        String maintainer,        String uploaders,        String checkSum,        String priority,        String description    ) {
        super(
        );
        this.tag = tag;
        this.section = section;
        this.maintainer = maintainer;
        this.uploaders = uploaders;
        this.checkSum = checkSum;
        this.priority = priority;
        this.description = description;
    }


    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }
    public String getMaintainer() {
        return maintainer;
    }

    public void setMaintainer(String maintainer) {
        this.maintainer = maintainer;
    }
    public String getUploaders() {
        return uploaders;
    }

    public void setUploaders(String uploaders) {
        this.uploaders = uploaders;
    }
    public String getChecksum() {
        return checkSum;
    }

    public void setChecksum(String checkSum) {
        this.checkSum = checkSum;
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

    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }

}