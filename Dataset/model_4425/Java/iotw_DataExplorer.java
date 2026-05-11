





import java.util.List;
import java.util.ArrayList;

public class iotw_DataExplorer  {






    private iotw_DataControl iotw_datacontrol;




    private List<iotw_DataControl> iotw_datacontrols;


    public iotw_DataExplorer(
    ) {
        this.iotw_datacontrols = new ArrayList<>();
    }

    public iotw_DataExplorer(
        ArrayList<iotw_DataControl> iotw_datacontrols    ) {
        this.iotw_datacontrols = iotw_datacontrols;
    }


    public iotw_DataControl getIotw_datacontrol() {
        return iotw_datacontrol;
    }

    public void setIotw_datacontrol(iotw_DataControl iotw_datacontrol) {
        this.iotw_datacontrol = iotw_datacontrol;
    }
    public List<iotw_DataControl> getIotw_datacontrols() {
        return iotw_datacontrols;
    }

    public void addIotw_datacontrol(Iotw_datacontrol iotw_datacontrol) {
        this.iotw_datacontrols.add(iotw_datacontrol);
    }

}