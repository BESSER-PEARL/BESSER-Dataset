





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDataField  {

    private String fieldName;
    private String fieldType;
    private boolean isKey;
    private int maxMultiplicity;





    private ddsMetamodel_DdsDataStructure ddsmetamodel_ddsdatastructure;


    public ddsMetamodel_DdsDataField(
        String fieldName,        String fieldType,        boolean isKey,        int maxMultiplicity    ) {
        this.fieldName = fieldName;
        this.fieldType = fieldType;
        this.isKey = isKey;
        this.maxMultiplicity = maxMultiplicity;
    }


    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }
    public String getFieldtype() {
        return fieldType;
    }

    public void setFieldtype(String fieldType) {
        this.fieldType = fieldType;
    }
    public boolean getIskey() {
        return isKey;
    }

    public void setIskey(boolean isKey) {
        this.isKey = isKey;
    }
    public int getMaxmultiplicity() {
        return maxMultiplicity;
    }

    public void setMaxmultiplicity(int maxMultiplicity) {
        this.maxMultiplicity = maxMultiplicity;
    }

    public ddsMetamodel_DdsDataStructure getDdsmetamodel_ddsdatastructure() {
        return ddsmetamodel_ddsdatastructure;
    }

    public void setDdsmetamodel_ddsdatastructure(ddsMetamodel_DdsDataStructure ddsmetamodel_ddsdatastructure) {
        this.ddsmetamodel_ddsdatastructure = ddsmetamodel_ddsdatastructure;
    }

}