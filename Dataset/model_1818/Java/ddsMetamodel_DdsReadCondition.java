





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsReadCondition  {

    private String view_state_mask;
    private String instance_state_mask;
    private String sample_state_mask;





    private ddsMetamodel_DdsDataReader ddsmetamodel_ddsdatareader;




    private ddsMetamodel_DdsWaitSet ddsmetamodel_ddswaitset;


    public ddsMetamodel_DdsReadCondition(
        String view_state_mask,        String instance_state_mask,        String sample_state_mask    ) {
        this.view_state_mask = view_state_mask;
        this.instance_state_mask = instance_state_mask;
        this.sample_state_mask = sample_state_mask;
    }


    public String getView_state_mask() {
        return view_state_mask;
    }

    public void setView_state_mask(String view_state_mask) {
        this.view_state_mask = view_state_mask;
    }
    public String getInstance_state_mask() {
        return instance_state_mask;
    }

    public void setInstance_state_mask(String instance_state_mask) {
        this.instance_state_mask = instance_state_mask;
    }
    public String getSample_state_mask() {
        return sample_state_mask;
    }

    public void setSample_state_mask(String sample_state_mask) {
        this.sample_state_mask = sample_state_mask;
    }

    public ddsMetamodel_DdsDataReader getDdsmetamodel_ddsdatareader() {
        return ddsmetamodel_ddsdatareader;
    }

    public void setDdsmetamodel_ddsdatareader(ddsMetamodel_DdsDataReader ddsmetamodel_ddsdatareader) {
        this.ddsmetamodel_ddsdatareader = ddsmetamodel_ddsdatareader;
    }
    public ddsMetamodel_DdsWaitSet getDdsmetamodel_ddswaitset() {
        return ddsmetamodel_ddswaitset;
    }

    public void setDdsmetamodel_ddswaitset(ddsMetamodel_DdsWaitSet ddsmetamodel_ddswaitset) {
        this.ddsmetamodel_ddswaitset = ddsmetamodel_ddswaitset;
    }

}