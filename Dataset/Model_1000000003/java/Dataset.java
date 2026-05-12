





import java.util.List;
import java.util.ArrayList;

public class Dataset extends Element {

    private None licensing;
    private String source;
    private None dataset_type;
    private String version;



    public Dataset(
        None licensing,        String source,        None dataset_type,        String version    ) {
        super(
        );
        this.licensing = licensing;
        this.source = source;
        this.dataset_type = dataset_type;
        this.version = version;
    }


    public None getLicensing() {
        return licensing;
    }

    public void setLicensing(None licensing) {
        this.licensing = licensing;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public None getDataset_type() {
        return dataset_type;
    }

    public void setDataset_type(None dataset_type) {
        this.dataset_type = dataset_type;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}