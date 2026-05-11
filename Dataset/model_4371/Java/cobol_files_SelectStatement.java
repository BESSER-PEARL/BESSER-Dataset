





import java.util.List;
import java.util.ArrayList;

public class cobol_files_SelectStatement extends IncompleteElement {

    private String externalFileNames;
    private boolean isOptional;





    private FileNameReference filenamereference;


    public cobol_files_SelectStatement(
        String externalFileNames,        boolean isOptional    ) {
        super(
        );
        this.externalFileNames = externalFileNames;
        this.isOptional = isOptional;
    }


    public String getExternalfilenames() {
        return externalFileNames;
    }

    public void setExternalfilenames(String externalFileNames) {
        this.externalFileNames = externalFileNames;
    }
    public boolean getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(boolean isOptional) {
        this.isOptional = isOptional;
    }

    public FileNameReference getFilenamereference() {
        return filenamereference;
    }

    public void setFilenamereference(FileNameReference filenamereference) {
        this.filenamereference = filenamereference;
    }

}