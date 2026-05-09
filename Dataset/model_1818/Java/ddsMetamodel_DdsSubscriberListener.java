





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsSubscriberListener  {

    private String listenedStatus;
    private String name;



    public ddsMetamodel_DdsSubscriberListener(
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


}