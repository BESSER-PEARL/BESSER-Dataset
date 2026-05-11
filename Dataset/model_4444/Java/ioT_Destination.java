





import java.util.List;
import java.util.ArrayList;

public class ioT_Destination  {

    private String name;





    private ioT_DestinationType iot_destinationtype;


    public ioT_Destination(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ioT_DestinationType getIot_destinationtype() {
        return iot_destinationtype;
    }

    public void setIot_destinationtype(ioT_DestinationType iot_destinationtype) {
        this.iot_destinationtype = iot_destinationtype;
    }

}