





import java.util.List;
import java.util.ArrayList;

public class gast_core_Directory extends NamedModelElement {

    private String fullQualifiedPath;
    private String fileSystemPath;





    private List<Directory> directorys;




    private Directory directory;


    public gast_core_Directory(
        String fullQualifiedPath,        String fileSystemPath    ) {
        super(
        );
        this.fullQualifiedPath = fullQualifiedPath;
        this.fileSystemPath = fileSystemPath;
        this.directorys = new ArrayList<>();
    }

    public gast_core_Directory(
        String fullQualifiedPath,        String fileSystemPath        ArrayList<Directory> directorys    ) {
        this.fullQualifiedPath = fullQualifiedPath;
        this.fileSystemPath = fileSystemPath;
        this.directorys = directorys;
    }

    public String getFullqualifiedpath() {
        return fullQualifiedPath;
    }

    public void setFullqualifiedpath(String fullQualifiedPath) {
        this.fullQualifiedPath = fullQualifiedPath;
    }
    public String getFilesystempath() {
        return fileSystemPath;
    }

    public void setFilesystempath(String fileSystemPath) {
        this.fileSystemPath = fileSystemPath;
    }

    public List<Directory> getDirectorys() {
        return directorys;
    }

    public void addDirectory(Directory directory) {
        this.directorys.add(directory);
    }
    public Directory getDirectory() {
        return directory;
    }

    public void setDirectory(Directory directory) {
        this.directory = directory;
    }

}