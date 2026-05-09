





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_File extends NamedElement {

    private boolean suid;
    private boolean isMissing;
    private String permission;
    private boolean guid;
    private String description;
    private String checkSum;
    private boolean isDirectory;
    private String extension;
    private String location;
    private int size;





    private mancoosimm_SGMLDocument mancoosimm_sgmldocument;




    private mancoosimm_SGMLDocument mancoosimm_sgmldocument;




    private List<mancoosimm_File> mancoosimm_files;




    private mancoosimm_EmacsPackage mancoosimm_emacspackage;




    private mancoosimm_File mancoosimm_file;


    public mancoosimm_File(
        boolean suid,        boolean isMissing,        String permission,        boolean guid,        String description,        String checkSum,        boolean isDirectory,        String extension,        String location,        int size    ) {
        super(
        );
        this.suid = suid;
        this.isMissing = isMissing;
        this.permission = permission;
        this.guid = guid;
        this.description = description;
        this.checkSum = checkSum;
        this.isDirectory = isDirectory;
        this.extension = extension;
        this.location = location;
        this.size = size;
        this.mancoosimm_files = new ArrayList<>();
    }

    public mancoosimm_File(
        boolean suid,        boolean isMissing,        String permission,        boolean guid,        String description,        String checkSum,        boolean isDirectory,        String extension,        String location,        int size        ArrayList<mancoosimm_File> mancoosimm_files    ) {
        this.suid = suid;
        this.isMissing = isMissing;
        this.permission = permission;
        this.guid = guid;
        this.description = description;
        this.checkSum = checkSum;
        this.isDirectory = isDirectory;
        this.extension = extension;
        this.location = location;
        this.size = size;
        this.mancoosimm_files = mancoosimm_files;
    }

    public boolean getSuid() {
        return suid;
    }

    public void setSuid(boolean suid) {
        this.suid = suid;
    }
    public boolean getIsmissing() {
        return isMissing;
    }

    public void setIsmissing(boolean isMissing) {
        this.isMissing = isMissing;
    }
    public String getPermission() {
        return permission;
    }

    public void setPermission(String permission) {
        this.permission = permission;
    }
    public boolean getGuid() {
        return guid;
    }

    public void setGuid(boolean guid) {
        this.guid = guid;
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
    public boolean getIsdirectory() {
        return isDirectory;
    }

    public void setIsdirectory(boolean isDirectory) {
        this.isDirectory = isDirectory;
    }
    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public mancoosimm_SGMLDocument getMancoosimm_sgmldocument() {
        return mancoosimm_sgmldocument;
    }

    public void setMancoosimm_sgmldocument(mancoosimm_SGMLDocument mancoosimm_sgmldocument) {
        this.mancoosimm_sgmldocument = mancoosimm_sgmldocument;
    }
    public mancoosimm_SGMLDocument getMancoosimm_sgmldocument() {
        return mancoosimm_sgmldocument;
    }

    public void setMancoosimm_sgmldocument(mancoosimm_SGMLDocument mancoosimm_sgmldocument) {
        this.mancoosimm_sgmldocument = mancoosimm_sgmldocument;
    }
    public List<mancoosimm_File> getMancoosimm_files() {
        return mancoosimm_files;
    }

    public void addMancoosimm_file(Mancoosimm_file mancoosimm_file) {
        this.mancoosimm_files.add(mancoosimm_file);
    }
    public mancoosimm_EmacsPackage getMancoosimm_emacspackage() {
        return mancoosimm_emacspackage;
    }

    public void setMancoosimm_emacspackage(mancoosimm_EmacsPackage mancoosimm_emacspackage) {
        this.mancoosimm_emacspackage = mancoosimm_emacspackage;
    }
    public mancoosimm_File getMancoosimm_file() {
        return mancoosimm_file;
    }

    public void setMancoosimm_file(mancoosimm_File mancoosimm_file) {
        this.mancoosimm_file = mancoosimm_file;
    }

}