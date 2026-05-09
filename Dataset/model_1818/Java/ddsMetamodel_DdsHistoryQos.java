





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsHistoryQos  {

    private String kind;
    private String depth;





    private ddsMetamodel_DdsTopicQosProfile ddsmetamodel_ddstopicqosprofile;




    private ddsMetamodel_DdsDataReaderQosProfile ddsmetamodel_ddsdatareaderqosprofile;




    private ddsMetamodel_DdsDataWriterQosProfile ddsmetamodel_ddsdatawriterqosprofile;


    public ddsMetamodel_DdsHistoryQos(
        String kind,        String depth    ) {
        this.kind = kind;
        this.depth = depth;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getDepth() {
        return depth;
    }

    public void setDepth(String depth) {
        this.depth = depth;
    }

    public ddsMetamodel_DdsTopicQosProfile getDdsmetamodel_ddstopicqosprofile() {
        return ddsmetamodel_ddstopicqosprofile;
    }

    public void setDdsmetamodel_ddstopicqosprofile(ddsMetamodel_DdsTopicQosProfile ddsmetamodel_ddstopicqosprofile) {
        this.ddsmetamodel_ddstopicqosprofile = ddsmetamodel_ddstopicqosprofile;
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

}