





import java.util.List;
import java.util.ArrayList;

public class dcps_Domain extends Entity {

    private String domainId;





    private dcps_DomainParticipant dcps_domainparticipant;


    public dcps_Domain(
        String domainId    ) {
        super(
        );
        this.domainId = domainId;
    }


    public String getDomainid() {
        return domainId;
    }

    public void setDomainid(String domainId) {
        this.domainId = domainId;
    }

    public dcps_DomainParticipant getDcps_domainparticipant() {
        return dcps_domainparticipant;
    }

    public void setDcps_domainparticipant(dcps_DomainParticipant dcps_domainparticipant) {
        this.dcps_domainparticipant = dcps_domainparticipant;
    }

}