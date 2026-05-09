





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_InstalledPackage extends Package {

    private int fileSize;
    private String uploaders;
    private String tag;
    private int installedSize;
    private String priority;
    private String maintainer;
    private String section;
    private String description;
    private String checkSum;





    private mancoosimm_Configuration mancoosimm_configuration;




    private mancoosimm_InstalledPackage mancoosimm_installedpackage;




    private List<mancoosimm_InstalledPackage> mancoosimm_installedpackages;




    private List<mancoosimm_InstalledPackage> mancoosimm_installedpackages;




    private mancoosimm_InstalledPackage mancoosimm_installedpackage;




    private mancoosimm_InstalledPackage mancoosimm_installedpackage;


    public mancoosimm_InstalledPackage(
        int fileSize,        String uploaders,        String tag,        int installedSize,        String priority,        String maintainer,        String section,        String description,        String checkSum    ) {
        super(
        );
        this.fileSize = fileSize;
        this.uploaders = uploaders;
        this.tag = tag;
        this.installedSize = installedSize;
        this.priority = priority;
        this.maintainer = maintainer;
        this.section = section;
        this.description = description;
        this.checkSum = checkSum;
        this.mancoosimm_installedpackages = new ArrayList<>();
        this.mancoosimm_installedpackages = new ArrayList<>();
    }

    public mancoosimm_InstalledPackage(
        int fileSize,        String uploaders,        String tag,        int installedSize,        String priority,        String maintainer,        String section,        String description,        String checkSum        ArrayList<mancoosimm_InstalledPackage> mancoosimm_installedpackages,        ArrayList<mancoosimm_InstalledPackage> mancoosimm_installedpackages    ) {
        this.fileSize = fileSize;
        this.uploaders = uploaders;
        this.tag = tag;
        this.installedSize = installedSize;
        this.priority = priority;
        this.maintainer = maintainer;
        this.section = section;
        this.description = description;
        this.checkSum = checkSum;
        this.mancoosimm_installedpackages = mancoosimm_installedpackages;
        this.mancoosimm_installedpackages = mancoosimm_installedpackages;
    }

    public int getFilesize() {
        return fileSize;
    }

    public void setFilesize(int fileSize) {
        this.fileSize = fileSize;
    }
    public String getUploaders() {
        return uploaders;
    }

    public void setUploaders(String uploaders) {
        this.uploaders = uploaders;
    }
    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }
    public int getInstalledsize() {
        return installedSize;
    }

    public void setInstalledsize(int installedSize) {
        this.installedSize = installedSize;
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
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getChecksum() {
        return checkSum;
    }

    public void setChecksum(String checkSum) {
        this.checkSum = checkSum;
    }

    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }
    public mancoosimm_InstalledPackage getMancoosimm_installedpackage() {
        return mancoosimm_installedpackage;
    }

    public void setMancoosimm_installedpackage(mancoosimm_InstalledPackage mancoosimm_installedpackage) {
        this.mancoosimm_installedpackage = mancoosimm_installedpackage;
    }
    public List<mancoosimm_InstalledPackage> getMancoosimm_installedpackages() {
        return mancoosimm_installedpackages;
    }

    public void addMancoosimm_installedpackage(Mancoosimm_installedpackage mancoosimm_installedpackage) {
        this.mancoosimm_installedpackages.add(mancoosimm_installedpackage);
    }
    public List<mancoosimm_InstalledPackage> getMancoosimm_installedpackages() {
        return mancoosimm_installedpackages;
    }

    public void addMancoosimm_installedpackage(Mancoosimm_installedpackage mancoosimm_installedpackage) {
        this.mancoosimm_installedpackages.add(mancoosimm_installedpackage);
    }
    public mancoosimm_InstalledPackage getMancoosimm_installedpackage() {
        return mancoosimm_installedpackage;
    }

    public void setMancoosimm_installedpackage(mancoosimm_InstalledPackage mancoosimm_installedpackage) {
        this.mancoosimm_installedpackage = mancoosimm_installedpackage;
    }
    public mancoosimm_InstalledPackage getMancoosimm_installedpackage() {
        return mancoosimm_installedpackage;
    }

    public void setMancoosimm_installedpackage(mancoosimm_InstalledPackage mancoosimm_installedpackage) {
        this.mancoosimm_installedpackage = mancoosimm_installedpackage;
    }

}