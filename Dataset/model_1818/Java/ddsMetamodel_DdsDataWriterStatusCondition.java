





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDataWriterStatusCondition extends DdsStatusCondition {

    private String enabled_status;





    private ddsMetamodel_DdsDataWriter ddsmetamodel_ddsdatawriter;


    public ddsMetamodel_DdsDataWriterStatusCondition(
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

    public ddsMetamodel_DdsDataWriter getDdsmetamodel_ddsdatawriter() {
        return ddsmetamodel_ddsdatawriter;
    }

    public void setDdsmetamodel_ddsdatawriter(ddsMetamodel_DdsDataWriter ddsmetamodel_ddsdatawriter) {
        this.ddsmetamodel_ddsdatawriter = ddsmetamodel_ddsdatawriter;
    }

}