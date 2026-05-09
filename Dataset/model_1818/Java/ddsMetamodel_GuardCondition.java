





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_GuardCondition  {

    private String name;





    private ddsMetamodel_DdsWaitSet ddsmetamodel_ddswaitset;


    public ddsMetamodel_GuardCondition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ddsMetamodel_DdsWaitSet getDdsmetamodel_ddswaitset() {
        return ddsmetamodel_ddswaitset;
    }

    public void setDdsmetamodel_ddswaitset(ddsMetamodel_DdsWaitSet ddsmetamodel_ddswaitset) {
        this.ddsmetamodel_ddswaitset = ddsmetamodel_ddswaitset;
    }

}