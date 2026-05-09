





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDataReaderStatusCondition extends DdsStatusCondition {

    private String enabled_status;





    private ddsMetamodel_DdsDataReader ddsmetamodel_ddsdatareader;


    public ddsMetamodel_DdsDataReaderStatusCondition(
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

    public ddsMetamodel_DdsDataReader getDdsmetamodel_ddsdatareader() {
        return ddsmetamodel_ddsdatareader;
    }

    public void setDdsmetamodel_ddsdatareader(ddsMetamodel_DdsDataReader ddsmetamodel_ddsdatareader) {
        this.ddsmetamodel_ddsdatareader = ddsmetamodel_ddsdatareader;
    }

}