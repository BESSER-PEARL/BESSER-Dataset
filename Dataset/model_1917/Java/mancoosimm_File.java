





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_File extends NamedElement {

    private String location;
    private int size;
    private boolean guid;
    private boolean isMissing;
    private String checkSum;
    private String permission;
    private boolean isDirectory;
    private String extension;
    private String description;
    private boolean suid;





    private List<mancoosimm_PackageSetting> mancoosimm_packagesettings;




    private mancoosimm_PackageSetting mancoosimm_packagesetting;




    private mancoosimm_File mancoosimm_file;




    private mancoosimm_EmacsPackage mancoosimm_emacspackage;




    private mancoosimm_Module mancoosimm_module;




    private mancoosimm_FileSystem mancoosimm_filesystem;




    private mancoosimm_FileSystem mancoosimm_filesystem;




    private mancoosimm_UnpackedPackage mancoosimm_unpackedpackage;




    private List<mancoosimm_File> mancoosimm_files;




    private mancoosimm_FileSystem mancoosimm_filesystem;




    private mancoosimm_InstalledPackage mancoosimm_installedpackage;


    public mancoosimm_File(
        String location,        int size,        boolean guid,        boolean isMissing,        String checkSum,        String permission,        boolean isDirectory,        String extension,        String description,        boolean suid    ) {
        super(
        );
        this.location = location;
        this.size = size;
        this.guid = guid;
        this.isMissing = isMissing;
        this.checkSum = checkSum;
        this.permission = permission;
        this.isDirectory = isDirectory;
        this.extension = extension;
        this.description = description;
        this.suid = suid;
        this.mancoosimm_packagesettings = new ArrayList<>();
        this.mancoosimm_files = new ArrayList<>();
    }

    public mancoosimm_File(
        String location,        int size,        boolean guid,        boolean isMissing,        String checkSum,        String permission,        boolean isDirectory,        String extension,        String description,        boolean suid        ArrayList<mancoosimm_PackageSetting> mancoosimm_packagesettings,        ArrayList<mancoosimm_File> mancoosimm_files    ) {
        this.location = location;
        this.size = size;
        this.guid = guid;
        this.isMissing = isMissing;
        this.checkSum = checkSum;
        this.permission = permission;
        this.isDirectory = isDirectory;
        this.extension = extension;
        this.description = description;
        this.suid = suid;
        this.mancoosimm_packagesettings = mancoosimm_packagesettings;
        this.mancoosimm_files = mancoosimm_files;
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
    public boolean getGuid() {
        return guid;
    }

    public void setGuid(boolean guid) {
        this.guid = guid;
    }
    public boolean getIsmissing() {
        return isMissing;
    }

    public void setIsmissing(boolean isMissing) {
        this.isMissing = isMissing;
    }
    public String getChecksum() {
        return checkSum;
    }

    public void setChecksum(String checkSum) {
        this.checkSum = checkSum;
    }
    public String getPermission() {
        return permission;
    }

    public void setPermission(String permission) {
        this.permission = permission;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getSuid() {
        return suid;
    }

    public void setSuid(boolean suid) {
        this.suid = suid;
    }

    public List<mancoosimm_PackageSetting> getMancoosimm_packagesettings() {
        return mancoosimm_packagesettings;
    }

    public void addMancoosimm_packagesetting(Mancoosimm_packagesetting mancoosimm_packagesetting) {
        this.mancoosimm_packagesettings.add(mancoosimm_packagesetting);
    }
    public mancoosimm_PackageSetting getMancoosimm_packagesetting() {
        return mancoosimm_packagesetting;
    }

    public void setMancoosimm_packagesetting(mancoosimm_PackageSetting mancoosimm_packagesetting) {
        this.mancoosimm_packagesetting = mancoosimm_packagesetting;
    }
    public mancoosimm_File getMancoosimm_file() {
        return mancoosimm_file;
    }

    public void setMancoosimm_file(mancoosimm_File mancoosimm_file) {
        this.mancoosimm_file = mancoosimm_file;
    }
    public mancoosimm_EmacsPackage getMancoosimm_emacspackage() {
        return mancoosimm_emacspackage;
    }

    public void setMancoosimm_emacspackage(mancoosimm_EmacsPackage mancoosimm_emacspackage) {
        this.mancoosimm_emacspackage = mancoosimm_emacspackage;
    }
    public mancoosimm_Module getMancoosimm_module() {
        return mancoosimm_module;
    }

    public void setMancoosimm_module(mancoosimm_Module mancoosimm_module) {
        this.mancoosimm_module = mancoosimm_module;
    }
    public mancoosimm_FileSystem getMancoosimm_filesystem() {
        return mancoosimm_filesystem;
    }

    public void setMancoosimm_filesystem(mancoosimm_FileSystem mancoosimm_filesystem) {
        this.mancoosimm_filesystem = mancoosimm_filesystem;
    }
    public mancoosimm_FileSystem getMancoosimm_filesystem() {
        return mancoosimm_filesystem;
    }

    public void setMancoosimm_filesystem(mancoosimm_FileSystem mancoosimm_filesystem) {
        this.mancoosimm_filesystem = mancoosimm_filesystem;
    }
    public mancoosimm_UnpackedPackage getMancoosimm_unpackedpackage() {
        return mancoosimm_unpackedpackage;
    }

    public void setMancoosimm_unpackedpackage(mancoosimm_UnpackedPackage mancoosimm_unpackedpackage) {
        this.mancoosimm_unpackedpackage = mancoosimm_unpackedpackage;
    }
    public List<mancoosimm_File> getMancoosimm_files() {
        return mancoosimm_files;
    }

    public void addMancoosimm_file(Mancoosimm_file mancoosimm_file) {
        this.mancoosimm_files.add(mancoosimm_file);
    }
    public mancoosimm_FileSystem getMancoosimm_filesystem() {
        return mancoosimm_filesystem;
    }

    public void setMancoosimm_filesystem(mancoosimm_FileSystem mancoosimm_filesystem) {
        this.mancoosimm_filesystem = mancoosimm_filesystem;
    }
    public mancoosimm_InstalledPackage getMancoosimm_installedpackage() {
        return mancoosimm_installedpackage;
    }

    public void setMancoosimm_installedpackage(mancoosimm_InstalledPackage mancoosimm_installedpackage) {
        this.mancoosimm_installedpackage = mancoosimm_installedpackage;
    }

}