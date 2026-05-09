





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_HalfInstalledPackage extends Package {

    private String checkSum;
    private String tag;
    private String section;
    private String maintainer;
    private String priority;
    private String uploaders;
    private String description;



    public mancoosimm_HalfInstalledPackage(
        String checkSum,        String tag,        String section,        String maintainer,        String priority,        String uploaders,        String description    ) {
        super(
        );
        this.checkSum = checkSum;
        this.tag = tag;
        this.section = section;
        this.maintainer = maintainer;
        this.priority = priority;
        this.uploaders = uploaders;
        this.description = description;
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
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getUploaders() {
        return uploaders;
    }

    public void setUploaders(String uploaders) {
        this.uploaders = uploaders;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}