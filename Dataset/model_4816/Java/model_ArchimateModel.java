





import java.util.List;
import java.util.ArrayList;

public class model_ArchimateModel extends Nameable, Properties, Identifier, ArchimateModelElement, FolderContainer {

    private String file;
    private String version;
    private String purpose;



    public model_ArchimateModel(
        String file,        String version,        String purpose    ) {
        super(
        );
        this.file = file;
        this.version = version;
        this.purpose = purpose;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }


}