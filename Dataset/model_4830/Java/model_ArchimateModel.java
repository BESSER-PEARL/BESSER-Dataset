





import java.util.List;
import java.util.ArrayList;

public class model_ArchimateModel extends ArchimateModelObject, Properties, FolderContainer {

    private String file;
    private String version;
    private String purpose;





    private model_Metadata model_metadata;


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

    public model_Metadata getModel_metadata() {
        return model_metadata;
    }

    public void setModel_metadata(model_Metadata model_metadata) {
        this.model_metadata = model_metadata;
    }

}