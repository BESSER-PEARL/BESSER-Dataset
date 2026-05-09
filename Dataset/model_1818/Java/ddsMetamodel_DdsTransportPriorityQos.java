





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsTransportPriorityQos  {

    private String value;





    private ddsMetamodel_DdsTopicQosProfile ddsmetamodel_ddstopicqosprofile;




    private ddsMetamodel_DdsDataWriterQosProfile ddsmetamodel_ddsdatawriterqosprofile;


    public ddsMetamodel_DdsTransportPriorityQos(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
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

}