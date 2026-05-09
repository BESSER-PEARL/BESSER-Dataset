





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsGroupDataQos  {

    private String value;





    private ddsMetamodel_DdsPublisherQosProfile ddsmetamodel_ddspublisherqosprofile;




    private ddsMetamodel_DdsSubscriberQosProfile ddsmetamodel_ddssubscriberqosprofile;


    public ddsMetamodel_DdsGroupDataQos(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
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