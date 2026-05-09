





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsPublisherListener  {

    private String listenedStatus;
    private String name;





    private ddsMetamodel_DdsPublisher ddsmetamodel_ddspublisher;


    public ddsMetamodel_DdsPublisherListener(
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

    public ddsMetamodel_DdsPublisher getDdsmetamodel_ddspublisher() {
        return ddsmetamodel_ddspublisher;
    }

    public void setDdsmetamodel_ddspublisher(ddsMetamodel_DdsPublisher ddsmetamodel_ddspublisher) {
        this.ddsmetamodel_ddspublisher = ddsmetamodel_ddspublisher;
    }

}