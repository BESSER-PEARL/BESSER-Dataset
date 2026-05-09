





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDataReaderListener  {

    private String name;
    private String listenedStatus;



    public ddsMetamodel_DdsDataReaderListener(
        String name,        String listenedStatus    ) {
        this.name = name;
        this.listenedStatus = listenedStatus;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getListenedstatus() {
        return listenedStatus;
    }

    public void setListenedstatus(String listenedStatus) {
        this.listenedStatus = listenedStatus;
    }


}