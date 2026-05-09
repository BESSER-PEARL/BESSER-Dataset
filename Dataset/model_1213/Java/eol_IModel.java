





import java.util.List;
import java.util.ArrayList;

public class eol_IModel extends EOLElement {

    private String iMetamodelDriver;



    public eol_IModel(
        String iMetamodelDriver    ) {
        super(
        );
        this.iMetamodelDriver = iMetamodelDriver;
    }


    public String getImetamodeldriver() {
        return iMetamodelDriver;
    }

    public void setImetamodeldriver(String iMetamodelDriver) {
        this.iMetamodelDriver = iMetamodelDriver;
    }


}