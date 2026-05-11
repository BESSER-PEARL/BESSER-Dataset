





import java.util.List;
import java.util.ArrayList;

public class gast_core_Directory extends NamedModelElement {

    private String fullQualifiedPath;
    private String fileSystemPath;



    public gast_core_Directory(
        String fullQualifiedPath,        String fileSystemPath    ) {
        super(
        );
        this.fullQualifiedPath = fullQualifiedPath;
        this.fileSystemPath = fileSystemPath;
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


}