





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsTopicStatusCondition extends DdsStatusCondition {

    private String enabled_status;





    private ddsMetamodel_DdsTopic ddsmetamodel_ddstopic;


    public ddsMetamodel_DdsTopicStatusCondition(
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

    public ddsMetamodel_DdsTopic getDdsmetamodel_ddstopic() {
        return ddsmetamodel_ddstopic;
    }

    public void setDdsmetamodel_ddstopic(ddsMetamodel_DdsTopic ddsmetamodel_ddstopic) {
        this.ddsmetamodel_ddstopic = ddsmetamodel_ddstopic;
    }

}