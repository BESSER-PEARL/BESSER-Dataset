





import java.util.List;
import java.util.ArrayList;

public class dataflownet_Channel extends NamedElement {






    private dataflownet_DataflowSystem dataflownet_dataflowsystem;




    private dataflownet_FiringRule dataflownet_firingrule;


    public dataflownet_Channel(
    ) {
        super(
        );
    }



    public dataflownet_DataflowSystem getDataflownet_dataflowsystem() {
        return dataflownet_dataflowsystem;
    }

    public void setDataflownet_dataflowsystem(dataflownet_DataflowSystem dataflownet_dataflowsystem) {
        this.dataflownet_dataflowsystem = dataflownet_dataflowsystem;
    }
    public dataflownet_FiringRule getDataflownet_firingrule() {
        return dataflownet_firingrule;
    }

    public void setDataflownet_firingrule(dataflownet_FiringRule dataflownet_firingrule) {
        this.dataflownet_firingrule = dataflownet_firingrule;
    }

}