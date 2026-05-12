





import java.util.List;
import java.util.ArrayList;

public class AISystem extends Element {

    private String version;
    private String source;
    private None licensing;
    private String settings;
    private String data;





    private List<Dataset> datasets;


    public AISystem(
        String version,        String source,        None licensing,        String settings,        String data    ) {
        super(
        );
        this.version = version;
        this.source = source;
        this.licensing = licensing;
        this.settings = settings;
        this.data = data;
        this.datasets = new ArrayList<>();
    }

    public AISystem(
        String version,        String source,        None licensing,        String settings,        String data        ArrayList<Dataset> datasets    ) {
        this.version = version;
        this.source = source;
        this.licensing = licensing;
        this.settings = settings;
        this.data = data;
        this.datasets = datasets;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public None getLicensing() {
        return licensing;
    }

    public void setLicensing(None licensing) {
        this.licensing = licensing;
    }
    public String getSettings() {
        return settings;
    }

    public void setSettings(String settings) {
        this.settings = settings;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public List<Dataset> getDatasets() {
        return datasets;
    }

    public void addDataset(Dataset dataset) {
        this.datasets.add(dataset);
    }

}