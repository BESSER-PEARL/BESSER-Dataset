





import java.util.List;
import java.util.ArrayList;

public class iotw_Mainboard  {

    private String name;





    private List<iotw_ConnectivityControl> iotw_connectivitycontrols;




    private iotw_ConnectivityControl iotw_connectivitycontrol;




    private List<iotw_IOControl> iotw_iocontrols;




    private iotw_IOControl iotw_iocontrol;


    public iotw_Mainboard(
        String name    ) {
        this.name = name;
        this.iotw_connectivitycontrols = new ArrayList<>();
        this.iotw_iocontrols = new ArrayList<>();
    }

    public iotw_Mainboard(
        String name        ArrayList<iotw_ConnectivityControl> iotw_connectivitycontrols,        ArrayList<iotw_IOControl> iotw_iocontrols    ) {
        this.name = name;
        this.iotw_connectivitycontrols = iotw_connectivitycontrols;
        this.iotw_iocontrols = iotw_iocontrols;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<iotw_ConnectivityControl> getIotw_connectivitycontrols() {
        return iotw_connectivitycontrols;
    }

    public void addIotw_connectivitycontrol(Iotw_connectivitycontrol iotw_connectivitycontrol) {
        this.iotw_connectivitycontrols.add(iotw_connectivitycontrol);
    }
    public iotw_ConnectivityControl getIotw_connectivitycontrol() {
        return iotw_connectivitycontrol;
    }

    public void setIotw_connectivitycontrol(iotw_ConnectivityControl iotw_connectivitycontrol) {
        this.iotw_connectivitycontrol = iotw_connectivitycontrol;
    }
    public List<iotw_IOControl> getIotw_iocontrols() {
        return iotw_iocontrols;
    }

    public void addIotw_iocontrol(Iotw_iocontrol iotw_iocontrol) {
        this.iotw_iocontrols.add(iotw_iocontrol);
    }
    public iotw_IOControl getIotw_iocontrol() {
        return iotw_iocontrol;
    }

    public void setIotw_iocontrol(iotw_IOControl iotw_iocontrol) {
        this.iotw_iocontrol = iotw_iocontrol;
    }

}