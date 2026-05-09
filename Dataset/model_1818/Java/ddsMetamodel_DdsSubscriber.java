





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsSubscriber  {

    private String subscriberName;





    private ddsMetamodel_DdsDomainParticipant ddsmetamodel_ddsdomainparticipant;




    private ddsMetamodel_DdsSubscriberListener ddsmetamodel_ddssubscriberlistener;




    private ddsMetamodel_DdsSubscriberQosProfile ddsmetamodel_ddssubscriberqosprofile;


    public ddsMetamodel_DdsSubscriber(
        String subscriberName    ) {
        this.subscriberName = subscriberName;
    }


    public String getSubscribername() {
        return subscriberName;
    }

    public void setSubscribername(String subscriberName) {
        this.subscriberName = subscriberName;
    }

    public ddsMetamodel_DdsDomainParticipant getDdsmetamodel_ddsdomainparticipant() {
        return ddsmetamodel_ddsdomainparticipant;
    }

    public void setDdsmetamodel_ddsdomainparticipant(ddsMetamodel_DdsDomainParticipant ddsmetamodel_ddsdomainparticipant) {
        this.ddsmetamodel_ddsdomainparticipant = ddsmetamodel_ddsdomainparticipant;
    }
    public ddsMetamodel_DdsSubscriberListener getDdsmetamodel_ddssubscriberlistener() {
        return ddsmetamodel_ddssubscriberlistener;
    }

    public void setDdsmetamodel_ddssubscriberlistener(ddsMetamodel_DdsSubscriberListener ddsmetamodel_ddssubscriberlistener) {
        this.ddsmetamodel_ddssubscriberlistener = ddsmetamodel_ddssubscriberlistener;
    }
    public ddsMetamodel_DdsSubscriberQosProfile getDdsmetamodel_ddssubscriberqosprofile() {
        return ddsmetamodel_ddssubscriberqosprofile;
    }

    public void setDdsmetamodel_ddssubscriberqosprofile(ddsMetamodel_DdsSubscriberQosProfile ddsmetamodel_ddssubscriberqosprofile) {
        this.ddsmetamodel_ddssubscriberqosprofile = ddsmetamodel_ddssubscriberqosprofile;
    }

}