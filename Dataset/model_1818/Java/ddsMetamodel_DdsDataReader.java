





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDataReader  {

    private String dataReaderName;





    private ddsMetamodel_DdsDataReaderListener ddsmetamodel_ddsdatareaderlistener;




    private ddsMetamodel_DdsSubscriber ddsmetamodel_ddssubscriber;




    private ddsMetamodel_DdsSubscriber ddsmetamodel_ddssubscriber;




    private ddsMetamodel_DdsTopic ddsmetamodel_ddstopic;


    public ddsMetamodel_DdsDataReader(
        String dataReaderName    ) {
        this.dataReaderName = dataReaderName;
    }


    public String getDatareadername() {
        return dataReaderName;
    }

    public void setDatareadername(String dataReaderName) {
        this.dataReaderName = dataReaderName;
    }

    public ddsMetamodel_DdsDataReaderListener getDdsmetamodel_ddsdatareaderlistener() {
        return ddsmetamodel_ddsdatareaderlistener;
    }

    public void setDdsmetamodel_ddsdatareaderlistener(ddsMetamodel_DdsDataReaderListener ddsmetamodel_ddsdatareaderlistener) {
        this.ddsmetamodel_ddsdatareaderlistener = ddsmetamodel_ddsdatareaderlistener;
    }
    public ddsMetamodel_DdsSubscriber getDdsmetamodel_ddssubscriber() {
        return ddsmetamodel_ddssubscriber;
    }

    public void setDdsmetamodel_ddssubscriber(ddsMetamodel_DdsSubscriber ddsmetamodel_ddssubscriber) {
        this.ddsmetamodel_ddssubscriber = ddsmetamodel_ddssubscriber;
    }
    public ddsMetamodel_DdsSubscriber getDdsmetamodel_ddssubscriber() {
        return ddsmetamodel_ddssubscriber;
    }

    public void setDdsmetamodel_ddssubscriber(ddsMetamodel_DdsSubscriber ddsmetamodel_ddssubscriber) {
        this.ddsmetamodel_ddssubscriber = ddsmetamodel_ddssubscriber;
    }
    public ddsMetamodel_DdsTopic getDdsmetamodel_ddstopic() {
        return ddsmetamodel_ddstopic;
    }

    public void setDdsmetamodel_ddstopic(ddsMetamodel_DdsTopic ddsmetamodel_ddstopic) {
        this.ddsmetamodel_ddstopic = ddsmetamodel_ddstopic;
    }

}