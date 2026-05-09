





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsPartitionQos  {

    private String name;





    private ddsMetamodel_DdsSubscriberQosProfile ddsmetamodel_ddssubscriberqosprofile;




    private ddsMetamodel_DdsPublisherQosProfile ddsmetamodel_ddspublisherqosprofile;


    public ddsMetamodel_DdsPartitionQos(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ddsMetamodel_DdsSubscriberQosProfile getDdsmetamodel_ddssubscriberqosprofile() {
        return ddsmetamodel_ddssubscriberqosprofile;
    }

    public void setDdsmetamodel_ddssubscriberqosprofile(ddsMetamodel_DdsSubscriberQosProfile ddsmetamodel_ddssubscriberqosprofile) {
        this.ddsmetamodel_ddssubscriberqosprofile = ddsmetamodel_ddssubscriberqosprofile;
    }
    public ddsMetamodel_DdsPublisherQosProfile getDdsmetamodel_ddspublisherqosprofile() {
        return ddsmetamodel_ddspublisherqosprofile;
    }

    public void setDdsmetamodel_ddspublisherqosprofile(ddsMetamodel_DdsPublisherQosProfile ddsmetamodel_ddspublisherqosprofile) {
        this.ddsmetamodel_ddspublisherqosprofile = ddsmetamodel_ddspublisherqosprofile;
    }

}