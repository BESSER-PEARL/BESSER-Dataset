





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_InstalledPackage extends Package {

    private String tag;
    private String section;
    private String description;
    private String uploaders;
    private String checkSum;
    private String priority;
    private int installedSize;
    private int fileSize;
    private String maintainer;





    private mancoosimm_InstalledPackage mancoosimm_installedpackage;




    private List<mancoosimm_InstalledPackage> mancoosimm_installedpackages;




    private List<mancoosimm_File> mancoosimm_files;




    private List<mancoosimm_InstalledPackage> mancoosimm_installedpackages;




    private mancoosimm_InstalledPackage mancoosimm_installedpackage;




    private mancoosimm_InstalledPackage mancoosimm_installedpackage;




    private mancoosimm_Configuration mancoosimm_configuration;


    public mancoosimm_InstalledPackage(
        String tag,        String section,        String description,        String uploaders,        String checkSum,        String priority,        int installedSize,        int fileSize,        String maintainer    ) {
        super(
        );
        this.tag = tag;
        this.section = section;
        this.description = description;
        this.uploaders = uploaders;
        this.checkSum = checkSum;
        this.priority = priority;
        this.installedSize = installedSize;
        this.fileSize = fileSize;
        this.maintainer = maintainer;
        this.mancoosimm_installedpackages = new ArrayList<>();
        this.mancoosimm_files = new ArrayList<>();
        this.mancoosimm_installedpackages = new ArrayList<>();
    }

    public mancoosimm_InstalledPackage(
        String tag,        String section,        String description,        String uploaders,        String checkSum,        String priority,        int installedSize,        int fileSize,        String maintainer        ArrayList<mancoosimm_InstalledPackage> mancoosimm_installedpackages,        ArrayList<mancoosimm_File> mancoosimm_files,        ArrayList<mancoosimm_InstalledPackage> mancoosimm_installedpackages    ) {
        this.tag = tag;
        this.section = section;
        this.description = description;
        this.uploaders = uploaders;
        this.checkSum = checkSum;
        this.priority = priority;
        this.installedSize = installedSize;
        this.fileSize = fileSize;
        this.maintainer = maintainer;
        this.mancoosimm_installedpackages = mancoosimm_installedpackages;
        this.mancoosimm_files = mancoosimm_files;
        this.mancoosimm_installedpackages = mancoosimm_installedpackages;
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
    public int getInstalledsize() {
        return installedSize;
    }

    public void setInstalledsize(int installedSize) {
        this.installedSize = installedSize;
    }
    public int getFilesize() {
        return fileSize;
    }

    public void setFilesize(int fileSize) {
        this.fileSize = fileSize;
    }
    public String getMaintainer() {
        return maintainer;
    }

    public void setMaintainer(String maintainer) {
        this.maintainer = maintainer;
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
    public List<mancoosimm_File> getMancoosimm_files() {
        return mancoosimm_files;
    }

    public void addMancoosimm_file(Mancoosimm_file mancoosimm_file) {
        this.mancoosimm_files.add(mancoosimm_file);
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
    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }

}