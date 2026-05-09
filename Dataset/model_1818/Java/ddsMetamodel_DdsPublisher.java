





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsPublisher  {

    private String publisherName;





    private ddsMetamodel_DdsDomainParticipant ddsmetamodel_ddsdomainparticipant;


    public ddsMetamodel_DdsPublisher(
        String publisherName    ) {
        this.publisherName = publisherName;
    }


    public String getPublishername() {
        return publisherName;
    }

    public void setPublishername(String publisherName) {
        this.publisherName = publisherName;
    }

    public ddsMetamodel_DdsDomainParticipant getDdsmetamodel_ddsdomainparticipant() {
        return ddsmetamodel_ddsdomainparticipant;
    }

    public void setDdsmetamodel_ddsdomainparticipant(ddsMetamodel_DdsDomainParticipant ddsmetamodel_ddsdomainparticipant) {
        this.ddsmetamodel_ddsdomainparticipant = ddsmetamodel_ddsdomainparticipant;
    }

}