





import java.util.List;
import java.util.ArrayList;

public class ioT_ServerTypes  {






    private List<ioT_ServerType> iot_servertypes;


    public ioT_ServerTypes(
    ) {
        this.iot_servertypes = new ArrayList<>();
    }

    public ioT_ServerTypes(
        ArrayList<ioT_ServerType> iot_servertypes    ) {
        this.iot_servertypes = iot_servertypes;
    }


    public List<ioT_ServerType> getIot_servertypes() {
        return iot_servertypes;
    }

    public void addIot_servertype(Iot_servertype iot_servertype) {
        this.iot_servertypes.add(iot_servertype);
    }

}