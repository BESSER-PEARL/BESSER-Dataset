





import java.util.List;
import java.util.ArrayList;

public class gast_core_Directory extends NamedModelElement {

    private String fileSystemPath;
    private String fullQualifiedPath;





    private BasePath basepath;


    public gast_core_Directory(
        String fileSystemPath,        String fullQualifiedPath    ) {
        super(
        );
        this.fileSystemPath = fileSystemPath;
        this.fullQualifiedPath = fullQualifiedPath;
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

    public BasePath getBasepath() {
        return basepath;
    }

    public void setBasepath(BasePath basepath) {
        this.basepath = basepath;
    }

}