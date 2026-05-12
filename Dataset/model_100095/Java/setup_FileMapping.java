





import java.util.List;
import java.util.ArrayList;

public class setup_FileMapping  {

    private String defaultEditorID;
    private String filePattern;





    private setup_FileAssociationsTask setup_fileassociationstask;


    public setup_FileMapping(
        String defaultEditorID,        String filePattern    ) {
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

    public setup_FileAssociationsTask getSetup_fileassociationstask() {
        return setup_fileassociationstask;
    }

    public void setSetup_fileassociationstask(setup_FileAssociationsTask setup_fileassociationstask) {
        this.setup_fileassociationstask = setup_fileassociationstask;
    }

}