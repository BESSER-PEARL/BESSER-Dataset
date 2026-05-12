





import java.util.List;
import java.util.ArrayList;

public class Datashape  {

    private String accepted_target_values;





    private List<Dataset> datasets;


    public Datashape(
        String accepted_target_values    ) {
        this.accepted_target_values = accepted_target_values;
        this.datasets = new ArrayList<>();
    }

    public Datashape(
        String accepted_target_values        ArrayList<Dataset> datasets    ) {
        this.accepted_target_values = accepted_target_values;
        this.datasets = datasets;
    }

    public String getAccepted_target_values() {
        return accepted_target_values;
    }

    public void setAccepted_target_values(String accepted_target_values) {
        this.accepted_target_values = accepted_target_values;
    }

    public List<Dataset> getDatasets() {
        return datasets;
    }

    public void addDataset(Dataset dataset) {
        this.datasets.add(dataset);
    }

}