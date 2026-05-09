





import java.util.List;
import java.util.ArrayList;

public class dcps_PublisherSubscriber extends DomainEntity {

    private int transportId;



    public dcps_PublisherSubscriber(
        int transportId    ) {
        super(
        );
        this.transportId = transportId;
    }


    public int getTransportid() {
        return transportId;
    }

    public void setTransportid(int transportId) {
        this.transportId = transportId;
    }


}