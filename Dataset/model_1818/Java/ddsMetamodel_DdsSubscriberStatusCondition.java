





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsSubscriberStatusCondition extends DdsStatusCondition {

    private String enabled_status;





    private ddsMetamodel_DdsSubscriber ddsmetamodel_ddssubscriber;


    public ddsMetamodel_DdsSubscriberStatusCondition(
        String enabled_status    ) {
        super(
        );
        this.enabled_status = enabled_status;
    }


    public String getEnabled_status() {
        return enabled_status;
    }

    public void setEnabled_status(String enabled_status) {
        this.enabled_status = enabled_status;
    }

    public ddsMetamodel_DdsSubscriber getDdsmetamodel_ddssubscriber() {
        return ddsmetamodel_ddssubscriber;
    }

    public void setDdsmetamodel_ddssubscriber(ddsMetamodel_DdsSubscriber ddsmetamodel_ddssubscriber) {
        this.ddsmetamodel_ddssubscriber = ddsmetamodel_ddssubscriber;
    }

}