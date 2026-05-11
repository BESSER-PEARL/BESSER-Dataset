





import java.util.List;
import java.util.ArrayList;

public class ioT_DestinationTypes  {






    private List<ioT_DestinationType> iot_destinationtypes;


    public ioT_DestinationTypes(
    ) {
        this.iot_destinationtypes = new ArrayList<>();
    }

    public ioT_DestinationTypes(
        ArrayList<ioT_DestinationType> iot_destinationtypes    ) {
        this.iot_destinationtypes = iot_destinationtypes;
    }


    public List<ioT_DestinationType> getIot_destinationtypes() {
        return iot_destinationtypes;
    }

    public void addIot_destinationtype(Iot_destinationtype iot_destinationtype) {
        this.iot_destinationtypes.add(iot_destinationtype);
    }

}