





import java.util.List;
import java.util.ArrayList;

public class dcps_Publisher extends PublisherSubscriber {






    private dcps_DomainParticipant dcps_domainparticipant;


    public dcps_Publisher(
    ) {
        super(
        );
    }



    public dcps_DomainParticipant getDcps_domainparticipant() {
        return dcps_domainparticipant;
    }

    public void setDcps_domainparticipant(dcps_DomainParticipant dcps_domainparticipant) {
        this.dcps_domainparticipant = dcps_domainparticipant;
    }

}