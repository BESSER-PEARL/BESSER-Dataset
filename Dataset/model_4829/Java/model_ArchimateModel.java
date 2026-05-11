





import java.util.List;
import java.util.ArrayList;

public class model_ArchimateModel extends FolderContainer, ArchimateModelObject, Properties {

    private String purpose;
    private String version;
    private String file;





    private model_Metadata model_metadata;


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

    public model_Metadata getModel_metadata() {
        return model_metadata;
    }

    public void setModel_metadata(model_Metadata model_metadata) {
        this.model_metadata = model_metadata;
    }

}