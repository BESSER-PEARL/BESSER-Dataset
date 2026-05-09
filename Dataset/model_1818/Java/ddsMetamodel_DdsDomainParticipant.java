





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDomainParticipant  {

    private int domainId;
    private String domainParticipantName;





    private ddsMetamodel_DdsApplication ddsmetamodel_ddsapplication;


    public ddsMetamodel_DdsDomainParticipant(
        int domainId,        String domainParticipantName    ) {
        this.domainId = domainId;
        this.domainParticipantName = domainParticipantName;
    }


    public int getDomainid() {
        return domainId;
    }

    public void setDomainid(int domainId) {
        this.domainId = domainId;
    }
    public String getDomainparticipantname() {
        return domainParticipantName;
    }

    public void setDomainparticipantname(String domainParticipantName) {
        this.domainParticipantName = domainParticipantName;
    }

    public ddsMetamodel_DdsApplication getDdsmetamodel_ddsapplication() {
        return ddsmetamodel_ddsapplication;
    }

    public void setDdsmetamodel_ddsapplication(ddsMetamodel_DdsApplication ddsmetamodel_ddsapplication) {
        this.ddsmetamodel_ddsapplication = ddsmetamodel_ddsapplication;
    }

}