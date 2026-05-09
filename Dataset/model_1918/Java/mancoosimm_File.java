





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_File extends NamedElement {

    private boolean guid;
    private boolean isMissing;
    private int size;
    private String description;
    private String location;
    private String checkSum;
    private String permission;
    private String extension;
    private boolean suid;
    private boolean isDirectory;





    private mancoosimm_Alternative mancoosimm_alternative;




    private mancoosimm_PackageSetting mancoosimm_packagesetting;




    private mancoosimm_SkeeperDocument mancoosimm_skeeperdocument;




    private mancoosimm_Service mancoosimm_service;




    private List<mancoosimm_File> mancoosimm_files;




    private mancoosimm_EmacsPackage mancoosimm_emacspackage;




    private mancoosimm_Alternative mancoosimm_alternative;




    private mancoosimm_MenuEntry mancoosimm_menuentry;




    private mancoosimm_User mancoosimm_user;




    private mancoosimm_Module mancoosimm_module;




    private mancoosimm_XFont mancoosimm_xfont;




    private mancoosimm_FileSystem mancoosimm_filesystem;




    private mancoosimm_User mancoosimm_user;




    private List<mancoosimm_PackageSetting> mancoosimm_packagesettings;




    private mancoosimm_FileSystem mancoosimm_filesystem;




    private mancoosimm_File mancoosimm_file;




    private mancoosimm_FileSystem mancoosimm_filesystem;




    private mancoosimm_SkeeperDocument mancoosimm_skeeperdocument;


    public mancoosimm_File(
        boolean guid,        boolean isMissing,        int size,        String description,        String location,        String checkSum,        String permission,        String extension,        boolean suid,        boolean isDirectory    ) {
        super(
        );
        this.guid = guid;
        this.isMissing = isMissing;
        this.size = size;
        this.description = description;
        this.location = location;
        this.checkSum = checkSum;
        this.permission = permission;
        this.extension = extension;
        this.suid = suid;
        this.isDirectory = isDirectory;
        this.mancoosimm_files = new ArrayList<>();
        this.mancoosimm_packagesettings = new ArrayList<>();
    }

    public mancoosimm_File(
        boolean guid,        boolean isMissing,        int size,        String description,        String location,        String checkSum,        String permission,        String extension,        boolean suid,        boolean isDirectory        ArrayList<mancoosimm_File> mancoosimm_files,        ArrayList<mancoosimm_PackageSetting> mancoosimm_packagesettings    ) {
        this.guid = guid;
        this.isMissing = isMissing;
        this.size = size;
        this.description = description;
        this.location = location;
        this.checkSum = checkSum;
        this.permission = permission;
        this.extension = extension;
        this.suid = suid;
        this.isDirectory = isDirectory;
        this.mancoosimm_files = mancoosimm_files;
        this.mancoosimm_packagesettings = mancoosimm_packagesettings;
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
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
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
    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public boolean getSuid() {
        return suid;
    }

    public void setSuid(boolean suid) {
        this.suid = suid;
    }
    public boolean getIsdirectory() {
        return isDirectory;
    }

    public void setIsdirectory(boolean isDirectory) {
        this.isDirectory = isDirectory;
    }

    public mancoosimm_Alternative getMancoosimm_alternative() {
        return mancoosimm_alternative;
    }

    public void setMancoosimm_alternative(mancoosimm_Alternative mancoosimm_alternative) {
        this.mancoosimm_alternative = mancoosimm_alternative;
    }
    public mancoosimm_PackageSetting getMancoosimm_packagesetting() {
        return mancoosimm_packagesetting;
    }

    public void setMancoosimm_packagesetting(mancoosimm_PackageSetting mancoosimm_packagesetting) {
        this.mancoosimm_packagesetting = mancoosimm_packagesetting;
    }
    public mancoosimm_SkeeperDocument getMancoosimm_skeeperdocument() {
        return mancoosimm_skeeperdocument;
    }

    public void setMancoosimm_skeeperdocument(mancoosimm_SkeeperDocument mancoosimm_skeeperdocument) {
        this.mancoosimm_skeeperdocument = mancoosimm_skeeperdocument;
    }
    public mancoosimm_Service getMancoosimm_service() {
        return mancoosimm_service;
    }

    public void setMancoosimm_service(mancoosimm_Service mancoosimm_service) {
        this.mancoosimm_service = mancoosimm_service;
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
    public mancoosimm_Alternative getMancoosimm_alternative() {
        return mancoosimm_alternative;
    }

    public void setMancoosimm_alternative(mancoosimm_Alternative mancoosimm_alternative) {
        this.mancoosimm_alternative = mancoosimm_alternative;
    }
    public mancoosimm_MenuEntry getMancoosimm_menuentry() {
        return mancoosimm_menuentry;
    }

    public void setMancoosimm_menuentry(mancoosimm_MenuEntry mancoosimm_menuentry) {
        this.mancoosimm_menuentry = mancoosimm_menuentry;
    }
    public mancoosimm_User getMancoosimm_user() {
        return mancoosimm_user;
    }

    public void setMancoosimm_user(mancoosimm_User mancoosimm_user) {
        this.mancoosimm_user = mancoosimm_user;
    }
    public mancoosimm_Module getMancoosimm_module() {
        return mancoosimm_module;
    }

    public void setMancoosimm_module(mancoosimm_Module mancoosimm_module) {
        this.mancoosimm_module = mancoosimm_module;
    }
    public mancoosimm_XFont getMancoosimm_xfont() {
        return mancoosimm_xfont;
    }

    public void setMancoosimm_xfont(mancoosimm_XFont mancoosimm_xfont) {
        this.mancoosimm_xfont = mancoosimm_xfont;
    }
    public mancoosimm_FileSystem getMancoosimm_filesystem() {
        return mancoosimm_filesystem;
    }

    public void setMancoosimm_filesystem(mancoosimm_FileSystem mancoosimm_filesystem) {
        this.mancoosimm_filesystem = mancoosimm_filesystem;
    }
    public mancoosimm_User getMancoosimm_user() {
        return mancoosimm_user;
    }

    public void setMancoosimm_user(mancoosimm_User mancoosimm_user) {
        this.mancoosimm_user = mancoosimm_user;
    }
    public List<mancoosimm_PackageSetting> getMancoosimm_packagesettings() {
        return mancoosimm_packagesettings;
    }

    public void addMancoosimm_packagesetting(Mancoosimm_packagesetting mancoosimm_packagesetting) {
        this.mancoosimm_packagesettings.add(mancoosimm_packagesetting);
    }
    public mancoosimm_FileSystem getMancoosimm_filesystem() {
        return mancoosimm_filesystem;
    }

    public void setMancoosimm_filesystem(mancoosimm_FileSystem mancoosimm_filesystem) {
        this.mancoosimm_filesystem = mancoosimm_filesystem;
    }
    public mancoosimm_File getMancoosimm_file() {
        return mancoosimm_file;
    }

    public void setMancoosimm_file(mancoosimm_File mancoosimm_file) {
        this.mancoosimm_file = mancoosimm_file;
    }
    public mancoosimm_FileSystem getMancoosimm_filesystem() {
        return mancoosimm_filesystem;
    }

    public void setMancoosimm_filesystem(mancoosimm_FileSystem mancoosimm_filesystem) {
        this.mancoosimm_filesystem = mancoosimm_filesystem;
    }
    public mancoosimm_SkeeperDocument getMancoosimm_skeeperdocument() {
        return mancoosimm_skeeperdocument;
    }

    public void setMancoosimm_skeeperdocument(mancoosimm_SkeeperDocument mancoosimm_skeeperdocument) {
        this.mancoosimm_skeeperdocument = mancoosimm_skeeperdocument;
    }

}