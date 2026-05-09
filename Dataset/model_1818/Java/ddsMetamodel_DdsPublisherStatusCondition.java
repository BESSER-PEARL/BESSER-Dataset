





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsPublisherStatusCondition extends DdsStatusCondition {

    private String enabled_status;





    private ddsMetamodel_DdsPublisher ddsmetamodel_ddspublisher;


    public ddsMetamodel_DdsPublisherStatusCondition(
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

    public ddsMetamodel_DdsPublisher getDdsmetamodel_ddspublisher() {
        return ddsmetamodel_ddspublisher;
    }

    public void setDdsmetamodel_ddspublisher(ddsMetamodel_DdsPublisher ddsmetamodel_ddspublisher) {
        this.ddsmetamodel_ddspublisher = ddsmetamodel_ddspublisher;
    }

}