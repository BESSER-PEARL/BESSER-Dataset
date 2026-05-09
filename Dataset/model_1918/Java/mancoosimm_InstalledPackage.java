





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_InstalledPackage extends Package {

    private String maintainer;
    private String tag;
    private String uploaders;
    private String priority;
    private int fileSize;
    private String description;
    private int installedSize;
    private String section;
    private String checkSum;





    private List<mancoosimm_InstalledPackage> mancoosimm_installedpackages;




    private List<mancoosimm_InstalledPackage> mancoosimm_installedpackages;




    private mancoosimm_Configuration mancoosimm_configuration;




    private mancoosimm_InstalledPackage mancoosimm_installedpackage;




    private List<mancoosimm_InstalledPackage> mancoosimm_installedpackages;




    private List<mancoosimm_File> mancoosimm_files;




    private mancoosimm_InstalledPackage mancoosimm_installedpackage;


    public mancoosimm_InstalledPackage(
        String maintainer,        String tag,        String uploaders,        String priority,        int fileSize,        String description,        int installedSize,        String section,        String checkSum    ) {
        super(
        );
        this.maintainer = maintainer;
        this.tag = tag;
        this.uploaders = uploaders;
        this.priority = priority;
        this.fileSize = fileSize;
        this.description = description;
        this.installedSize = installedSize;
        this.section = section;
        this.checkSum = checkSum;
        this.mancoosimm_installedpackages = new ArrayList<>();
        this.mancoosimm_installedpackages = new ArrayList<>();
        this.mancoosimm_installedpackages = new ArrayList<>();
        this.mancoosimm_files = new ArrayList<>();
    }

    public mancoosimm_InstalledPackage(
        String maintainer,        String tag,        String uploaders,        String priority,        int fileSize,        String description,        int installedSize,        String section,        String checkSum        ArrayList<mancoosimm_InstalledPackage> mancoosimm_installedpackages,        ArrayList<mancoosimm_InstalledPackage> mancoosimm_installedpackages,        ArrayList<mancoosimm_InstalledPackage> mancoosimm_installedpackages,        ArrayList<mancoosimm_File> mancoosimm_files    ) {
        this.maintainer = maintainer;
        this.tag = tag;
        this.uploaders = uploaders;
        this.priority = priority;
        this.fileSize = fileSize;
        this.description = description;
        this.installedSize = installedSize;
        this.section = section;
        this.checkSum = checkSum;
        this.mancoosimm_installedpackages = mancoosimm_installedpackages;
        this.mancoosimm_installedpackages = mancoosimm_installedpackages;
        this.mancoosimm_installedpackages = mancoosimm_installedpackages;
        this.mancoosimm_files = mancoosimm_files;
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
    public int getFilesize() {
        return fileSize;
    }

    public void setFilesize(int fileSize) {
        this.fileSize = fileSize;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getInstalledsize() {
        return installedSize;
    }

    public void setInstalledsize(int installedSize) {
        this.installedSize = installedSize;
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
    public List<mancoosimm_File> getMancoosimm_files() {
        return mancoosimm_files;
    }

    public void addMancoosimm_file(Mancoosimm_file mancoosimm_file) {
        this.mancoosimm_files.add(mancoosimm_file);
    }
    public mancoosimm_InstalledPackage getMancoosimm_installedpackage() {
        return mancoosimm_installedpackage;
    }

    public void setMancoosimm_installedpackage(mancoosimm_InstalledPackage mancoosimm_installedpackage) {
        this.mancoosimm_installedpackage = mancoosimm_installedpackage;
    }

}