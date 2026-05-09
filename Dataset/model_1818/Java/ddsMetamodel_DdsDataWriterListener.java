





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDataWriterListener  {

    private String listenedStatus;
    private String name;





    private ddsMetamodel_DdsDataWriter ddsmetamodel_ddsdatawriter;


    public ddsMetamodel_DdsDataWriterListener(
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

    public ddsMetamodel_DdsDataWriter getDdsmetamodel_ddsdatawriter() {
        return ddsmetamodel_ddsdatawriter;
    }

    public void setDdsmetamodel_ddsdatawriter(ddsMetamodel_DdsDataWriter ddsmetamodel_ddsdatawriter) {
        this.ddsmetamodel_ddsdatawriter = ddsmetamodel_ddsdatawriter;
    }

}