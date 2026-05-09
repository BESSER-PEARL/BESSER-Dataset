





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsOwnershipQos  {

    private String kind;





    private ddsMetamodel_DdsTopicQosProfile ddsmetamodel_ddstopicqosprofile;




    private ddsMetamodel_DdsDataWriterQosProfile ddsmetamodel_ddsdatawriterqosprofile;




    private ddsMetamodel_DdsDataReaderQosProfile ddsmetamodel_ddsdatareaderqosprofile;


    public ddsMetamodel_DdsOwnershipQos(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public ddsMetamodel_DdsTopicQosProfile getDdsmetamodel_ddstopicqosprofile() {
        return ddsmetamodel_ddstopicqosprofile;
    }

    public void setDdsmetamodel_ddstopicqosprofile(ddsMetamodel_DdsTopicQosProfile ddsmetamodel_ddstopicqosprofile) {
        this.ddsmetamodel_ddstopicqosprofile = ddsmetamodel_ddstopicqosprofile;
    }
    public ddsMetamodel_DdsDataWriterQosProfile getDdsmetamodel_ddsdatawriterqosprofile() {
        return ddsmetamodel_ddsdatawriterqosprofile;
    }

    public void setDdsmetamodel_ddsdatawriterqosprofile(ddsMetamodel_DdsDataWriterQosProfile ddsmetamodel_ddsdatawriterqosprofile) {
        this.ddsmetamodel_ddsdatawriterqosprofile = ddsmetamodel_ddsdatawriterqosprofile;
    }
    public ddsMetamodel_DdsDataReaderQosProfile getDdsmetamodel_ddsdatareaderqosprofile() {
        return ddsmetamodel_ddsdatareaderqosprofile;
    }

    public void setDdsmetamodel_ddsdatareaderqosprofile(ddsMetamodel_DdsDataReaderQosProfile ddsmetamodel_ddsdatareaderqosprofile) {
        this.ddsmetamodel_ddsdatareaderqosprofile = ddsmetamodel_ddsdatareaderqosprofile;
    }

}