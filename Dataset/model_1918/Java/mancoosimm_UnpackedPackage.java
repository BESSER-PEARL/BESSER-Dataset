





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_UnpackedPackage extends Package {

    private String checkSum;
    private String tag;
    private String maintainer;
    private String priority;
    private String section;
    private String uploaders;
    private String description;





    private mancoosimm_Configuration mancoosimm_configuration;




    private List<mancoosimm_File> mancoosimm_files;


    public mancoosimm_UnpackedPackage(
        String checkSum,        String tag,        String maintainer,        String priority,        String section,        String uploaders,        String description    ) {
        super(
        );
        this.checkSum = checkSum;
        this.tag = tag;
        this.maintainer = maintainer;
        this.priority = priority;
        this.section = section;
        this.uploaders = uploaders;
        this.description = description;
        this.mancoosimm_files = new ArrayList<>();
    }

    public mancoosimm_UnpackedPackage(
        String checkSum,        String tag,        String maintainer,        String priority,        String section,        String uploaders,        String description        ArrayList<mancoosimm_File> mancoosimm_files    ) {
        this.checkSum = checkSum;
        this.tag = tag;
        this.maintainer = maintainer;
        this.priority = priority;
        this.section = section;
        this.uploaders = uploaders;
        this.description = description;
        this.mancoosimm_files = mancoosimm_files;
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
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
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

    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }
    public List<mancoosimm_File> getMancoosimm_files() {
        return mancoosimm_files;
    }

    public void addMancoosimm_file(Mancoosimm_file mancoosimm_file) {
        this.mancoosimm_files.add(mancoosimm_file);
    }

}