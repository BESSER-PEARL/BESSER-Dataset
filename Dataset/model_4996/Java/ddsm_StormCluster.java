





import java.util.List;
import java.util.ArrayList;

public class ddsm_StormCluster extends Cluster {

    private String number_of_workers;



    public ddsm_StormCluster(
        String number_of_workers    ) {
        super(
        );
        this.number_of_workers = number_of_workers;
    }


    public String getNumber_of_workers() {
        return number_of_workers;
    }

    public void setNumber_of_workers(String number_of_workers) {
        this.number_of_workers = number_of_workers;
    }


}