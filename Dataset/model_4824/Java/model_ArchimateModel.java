





import java.util.List;
import java.util.ArrayList;

public class model_ArchimateModel extends Properties, ArchimateModelObject, FolderContainer {

    private String version;
    private String file;
    private String purpose;



    public model_ArchimateModel(
        String version,        String file,        String purpose    ) {
        super(
        );
        this.version = version;
        this.file = file;
        this.purpose = purpose;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }


}