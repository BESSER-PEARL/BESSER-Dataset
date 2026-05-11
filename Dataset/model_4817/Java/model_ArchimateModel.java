





import java.util.List;
import java.util.ArrayList;

public class model_ArchimateModel extends FolderContainer, ArchimateModelElement, Identifier, Nameable, Properties {

    private String purpose;
    private String version;
    private String file;



    public model_ArchimateModel(
        String purpose,        String version,        String file    ) {
        super(
        );
        this.purpose = purpose;
        this.version = version;
        this.file = file;
    }


    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
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


}