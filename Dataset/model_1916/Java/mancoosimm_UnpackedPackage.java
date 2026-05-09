





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_UnpackedPackage extends Package {

    private String tag;
    private String checkSum;
    private String priority;
    private String uploaders;
    private String description;
    private String maintainer;
    private String section;





    private mancoosimm_Configuration mancoosimm_configuration;




    private List<mancoosimm_File> mancoosimm_files;


    public mancoosimm_UnpackedPackage(
        String tag,        String checkSum,        String priority,        String uploaders,        String description,        String maintainer,        String section    ) {
        super(
        );
        this.tag = tag;
        this.checkSum = checkSum;
        this.priority = priority;
        this.uploaders = uploaders;
        this.description = description;
        this.maintainer = maintainer;
        this.section = section;
        this.mancoosimm_files = new ArrayList<>();
    }

    public mancoosimm_UnpackedPackage(
        String tag,        String checkSum,        String priority,        String uploaders,        String description,        String maintainer,        String section        ArrayList<mancoosimm_File> mancoosimm_files    ) {
        this.tag = tag;
        this.checkSum = checkSum;
        this.priority = priority;
        this.uploaders = uploaders;
        this.description = description;
        this.maintainer = maintainer;
        this.section = section;
        this.mancoosimm_files = mancoosimm_files;
    }

    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
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
    public String getMaintainer() {
        return maintainer;
    }

    public void setMaintainer(String maintainer) {
        this.maintainer = maintainer;
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
    public List<mancoosimm_File> getMancoosimm_files() {
        return mancoosimm_files;
    }

    public void addMancoosimm_file(Mancoosimm_file mancoosimm_file) {
        this.mancoosimm_files.add(mancoosimm_file);
    }

}