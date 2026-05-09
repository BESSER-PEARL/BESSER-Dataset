





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsTopicListener  {

    private String name;
    private String listenedStatus;





    private ddsMetamodel_DdsTopic ddsmetamodel_ddstopic;


    public ddsMetamodel_DdsTopicListener(
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

    public ddsMetamodel_DdsTopic getDdsmetamodel_ddstopic() {
        return ddsmetamodel_ddstopic;
    }

    public void setDdsmetamodel_ddstopic(ddsMetamodel_DdsTopic ddsmetamodel_ddstopic) {
        this.ddsmetamodel_ddstopic = ddsmetamodel_ddstopic;
    }

}