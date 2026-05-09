





import java.util.List;
import java.util.ArrayList;

public class dcps_DataWriter extends DataReaderWriter {






    private dcps_Publisher dcps_publisher;


    public dcps_DataWriter(
    ) {
        super(
        );
    }



    public dcps_Publisher getDcps_publisher() {
        return dcps_publisher;
    }

    public void setDcps_publisher(dcps_Publisher dcps_publisher) {
        this.dcps_publisher = dcps_publisher;
    }

}