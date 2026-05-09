





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsUserDataQos  {

    private String value;





    private ddsMetamodel_DdsDataReaderQosProfile ddsmetamodel_ddsdatareaderqosprofile;




    private ddsMetamodel_DdsDataWriterQosProfile ddsmetamodel_ddsdatawriterqosprofile;




    private ddsMetamodel_DdsDomainParticipantQosProfile ddsmetamodel_ddsdomainparticipantqosprofile;


    public ddsMetamodel_DdsUserDataQos(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public ddsMetamodel_DdsDataReaderQosProfile getDdsmetamodel_ddsdatareaderqosprofile() {
        return ddsmetamodel_ddsdatareaderqosprofile;
    }

    public void setDdsmetamodel_ddsdatareaderqosprofile(ddsMetamodel_DdsDataReaderQosProfile ddsmetamodel_ddsdatareaderqosprofile) {
        this.ddsmetamodel_ddsdatareaderqosprofile = ddsmetamodel_ddsdatareaderqosprofile;
    }
    public ddsMetamodel_DdsDataWriterQosProfile getDdsmetamodel_ddsdatawriterqosprofile() {
        return ddsmetamodel_ddsdatawriterqosprofile;
    }

    public void setDdsmetamodel_ddsdatawriterqosprofile(ddsMetamodel_DdsDataWriterQosProfile ddsmetamodel_ddsdatawriterqosprofile) {
        this.ddsmetamodel_ddsdatawriterqosprofile = ddsmetamodel_ddsdatawriterqosprofile;
    }
    public ddsMetamodel_DdsDomainParticipantQosProfile getDdsmetamodel_ddsdomainparticipantqosprofile() {
        return ddsmetamodel_ddsdomainparticipantqosprofile;
    }

    public void setDdsmetamodel_ddsdomainparticipantqosprofile(ddsMetamodel_DdsDomainParticipantQosProfile ddsmetamodel_ddsdomainparticipantqosprofile) {
        this.ddsmetamodel_ddsdomainparticipantqosprofile = ddsmetamodel_ddsdomainparticipantqosprofile;
    }

}