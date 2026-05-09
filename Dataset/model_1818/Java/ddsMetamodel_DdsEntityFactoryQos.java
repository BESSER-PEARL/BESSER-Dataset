





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsEntityFactoryQos  {

    private boolean autoenable_created_entities;





    private ddsMetamodel_DdsDomainParticipantQosProfile ddsmetamodel_ddsdomainparticipantqosprofile;




    private ddsMetamodel_DdsPublisherQosProfile ddsmetamodel_ddspublisherqosprofile;




    private ddsMetamodel_DdsSubscriberQosProfile ddsmetamodel_ddssubscriberqosprofile;


    public ddsMetamodel_DdsEntityFactoryQos(
        boolean autoenable_created_entities    ) {
        this.autoenable_created_entities = autoenable_created_entities;
    }


    public boolean getAutoenable_created_entities() {
        return autoenable_created_entities;
    }

    public void setAutoenable_created_entities(boolean autoenable_created_entities) {
        this.autoenable_created_entities = autoenable_created_entities;
    }

    public ddsMetamodel_DdsDomainParticipantQosProfile getDdsmetamodel_ddsdomainparticipantqosprofile() {
        return ddsmetamodel_ddsdomainparticipantqosprofile;
    }

    public void setDdsmetamodel_ddsdomainparticipantqosprofile(ddsMetamodel_DdsDomainParticipantQosProfile ddsmetamodel_ddsdomainparticipantqosprofile) {
        this.ddsmetamodel_ddsdomainparticipantqosprofile = ddsmetamodel_ddsdomainparticipantqosprofile;
    }
    public ddsMetamodel_DdsPublisherQosProfile getDdsmetamodel_ddspublisherqosprofile() {
        return ddsmetamodel_ddspublisherqosprofile;
    }

    public void setDdsmetamodel_ddspublisherqosprofile(ddsMetamodel_DdsPublisherQosProfile ddsmetamodel_ddspublisherqosprofile) {
        this.ddsmetamodel_ddspublisherqosprofile = ddsmetamodel_ddspublisherqosprofile;
    }
    public ddsMetamodel_DdsSubscriberQosProfile getDdsmetamodel_ddssubscriberqosprofile() {
        return ddsmetamodel_ddssubscriberqosprofile;
    }

    public void setDdsmetamodel_ddssubscriberqosprofile(ddsMetamodel_DdsSubscriberQosProfile ddsmetamodel_ddssubscriberqosprofile) {
        this.ddsmetamodel_ddssubscriberqosprofile = ddsmetamodel_ddssubscriberqosprofile;
    }

}