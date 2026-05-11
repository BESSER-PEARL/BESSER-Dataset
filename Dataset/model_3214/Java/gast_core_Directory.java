





import java.util.List;
import java.util.ArrayList;

public class gast_core_Directory extends NamedModelElement {

    private String fileSystemPath;
    private String fullQualifiedPath;





    private List<Directory> directorys;




    private Directory directory;


    public gast_core_Directory(
        String fileSystemPath,        String fullQualifiedPath    ) {
        super(
        );
        this.fileSystemPath = fileSystemPath;
        this.fullQualifiedPath = fullQualifiedPath;
        this.directorys = new ArrayList<>();
    }

    public gast_core_Directory(
        String fileSystemPath,        String fullQualifiedPath        ArrayList<Directory> directorys    ) {
        this.fileSystemPath = fileSystemPath;
        this.fullQualifiedPath = fullQualifiedPath;
        this.directorys = directorys;
    }

    public String getFilesystempath() {
        return fileSystemPath;
    }

    public void setFilesystempath(String fileSystemPath) {
        this.fileSystemPath = fileSystemPath;
    }
    public String getFullqualifiedpath() {
        return fullQualifiedPath;
    }

    public void setFullqualifiedpath(String fullQualifiedPath) {
        this.fullQualifiedPath = fullQualifiedPath;
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