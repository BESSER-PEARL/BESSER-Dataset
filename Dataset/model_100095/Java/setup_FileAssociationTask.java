





import java.util.List;
import java.util.ArrayList;

public class setup_FileAssociationTask extends SetupTask {

    private String defaultEditorID;
    private String filePattern;



    public setup_FileAssociationTask(
        String defaultEditorID,        String filePattern    ) {
        super(
        );
        this.defaultEditorID = defaultEditorID;
        this.filePattern = filePattern;
    }


    public String getDefaulteditorid() {
        return defaultEditorID;
    }

    public void setDefaulteditorid(String defaultEditorID) {
        this.defaultEditorID = defaultEditorID;
    }
    public String getFilepattern() {
        return filePattern;
    }

    public void setFilepattern(String filePattern) {
        this.filePattern = filePattern;
    }


}