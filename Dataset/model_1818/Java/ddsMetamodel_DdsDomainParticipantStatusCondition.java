





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDomainParticipantStatusCondition extends DdsStatusCondition {

    private String enabled_status;





    private ddsMetamodel_DdsDomainParticipant ddsmetamodel_ddsdomainparticipant;


    public ddsMetamodel_DdsDomainParticipantStatusCondition(
        String enabled_status    ) {
        super(
        );
        this.enabled_status = enabled_status;
    }


    public String getEnabled_status() {
        return enabled_status;
    }

    public void setEnabled_status(String enabled_status) {
        this.enabled_status = enabled_status;
    }

    public ddsMetamodel_DdsDomainParticipant getDdsmetamodel_ddsdomainparticipant() {
        return ddsmetamodel_ddsdomainparticipant;
    }

    public void setDdsmetamodel_ddsdomainparticipant(ddsMetamodel_DdsDomainParticipant ddsmetamodel_ddsdomainparticipant) {
        this.ddsmetamodel_ddsdomainparticipant = ddsmetamodel_ddsdomainparticipant;
    }

}