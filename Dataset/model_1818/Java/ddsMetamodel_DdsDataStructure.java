





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDataStructure  {

    private String structureName;





    private ddsMetamodel_DdsTopic ddsmetamodel_ddstopic;


    public ddsMetamodel_DdsDataStructure(
        String structureName    ) {
        this.structureName = structureName;
    }


    public String getStructurename() {
        return structureName;
    }

    public void setStructurename(String structureName) {
        this.structureName = structureName;
    }

    public ddsMetamodel_DdsTopic getDdsmetamodel_ddstopic() {
        return ddsmetamodel_ddstopic;
    }

    public void setDdsmetamodel_ddstopic(ddsMetamodel_DdsTopic ddsmetamodel_ddstopic) {
        this.ddsmetamodel_ddstopic = ddsmetamodel_ddstopic;
    }

}