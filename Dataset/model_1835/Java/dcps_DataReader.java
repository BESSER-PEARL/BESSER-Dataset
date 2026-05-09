





import java.util.List;
import java.util.ArrayList;

public class dcps_DataReader extends DataReaderWriter {






    private dcps_Subscriber dcps_subscriber;


    public dcps_DataReader(
    ) {
        super(
        );
    }



    public dcps_Subscriber getDcps_subscriber() {
        return dcps_subscriber;
    }

    public void setDcps_subscriber(dcps_Subscriber dcps_subscriber) {
        this.dcps_subscriber = dcps_subscriber;
    }

}