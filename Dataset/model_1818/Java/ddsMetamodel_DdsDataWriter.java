





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDataWriter  {

    private String dataWriterName;





    private ddsMetamodel_DdsTopic ddsmetamodel_ddstopic;




    private ddsMetamodel_DdsPublisher ddsmetamodel_ddspublisher;


    public ddsMetamodel_DdsDataWriter(
        String dataWriterName    ) {
        this.dataWriterName = dataWriterName;
    }


    public String getDatawritername() {
        return dataWriterName;
    }

    public void setDatawritername(String dataWriterName) {
        this.dataWriterName = dataWriterName;
    }

    public ddsMetamodel_DdsTopic getDdsmetamodel_ddstopic() {
        return ddsmetamodel_ddstopic;
    }

    public void setDdsmetamodel_ddstopic(ddsMetamodel_DdsTopic ddsmetamodel_ddstopic) {
        this.ddsmetamodel_ddstopic = ddsmetamodel_ddstopic;
    }
    public ddsMetamodel_DdsPublisher getDdsmetamodel_ddspublisher() {
        return ddsmetamodel_ddspublisher;
    }

    public void setDdsmetamodel_ddspublisher(ddsMetamodel_DdsPublisher ddsmetamodel_ddspublisher) {
        this.ddsmetamodel_ddspublisher = ddsmetamodel_ddspublisher;
    }

}