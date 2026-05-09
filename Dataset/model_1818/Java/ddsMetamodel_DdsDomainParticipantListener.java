





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDomainParticipantListener  {

    private String listenedStatus;
    private String name;





    private ddsMetamodel_DdsDomainParticipant ddsmetamodel_ddsdomainparticipant;


    public ddsMetamodel_DdsDomainParticipantListener(
        String listenedStatus,        String name    ) {
        this.listenedStatus = listenedStatus;
        this.name = name;
    }


    public String getListenedstatus() {
        return listenedStatus;
    }

    public void setListenedstatus(String listenedStatus) {
        this.listenedStatus = listenedStatus;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ddsMetamodel_DdsDomainParticipant getDdsmetamodel_ddsdomainparticipant() {
        return ddsmetamodel_ddsdomainparticipant;
    }

    public void setDdsmetamodel_ddsdomainparticipant(ddsMetamodel_DdsDomainParticipant ddsmetamodel_ddsdomainparticipant) {
        this.ddsmetamodel_ddsdomainparticipant = ddsmetamodel_ddsdomainparticipant;
    }

}