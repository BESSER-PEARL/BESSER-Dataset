





import java.util.List;
import java.util.ArrayList;

public class datasetload_DataSource  {

    private String Name;
    private boolean Connected;





    private datasetload_TableGroup datasetload_tablegroup;


    public datasetload_DataSource(
        String Name,        boolean Connected    ) {
        this.Name = Name;
        this.Connected = Connected;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public boolean getConnected() {
        return Connected;
    }

    public void setConnected(boolean Connected) {
        this.Connected = Connected;
    }

    public datasetload_TableGroup getDatasetload_tablegroup() {
        return datasetload_tablegroup;
    }

    public void setDatasetload_tablegroup(datasetload_TableGroup datasetload_tablegroup) {
        this.datasetload_tablegroup = datasetload_tablegroup;
    }

}