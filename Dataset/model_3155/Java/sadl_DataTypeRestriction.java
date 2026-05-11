





import java.util.List;
import java.util.ArrayList;

public class sadl_DataTypeRestriction  {

    private String basetype;
    private String basetypes;





    private sadl_UserDefinedDataType sadl_userdefineddatatype;


    public sadl_DataTypeRestriction(
        String basetype,        String basetypes    ) {
        this.basetype = basetype;
        this.basetypes = basetypes;
    }


    public String getBasetype() {
        return basetype;
    }

    public void setBasetype(String basetype) {
        this.basetype = basetype;
    }
    public String getBasetypes() {
        return basetypes;
    }

    public void setBasetypes(String basetypes) {
        this.basetypes = basetypes;
    }

    public sadl_UserDefinedDataType getSadl_userdefineddatatype() {
        return sadl_userdefineddatatype;
    }

    public void setSadl_userdefineddatatype(sadl_UserDefinedDataType sadl_userdefineddatatype) {
        this.sadl_userdefineddatatype = sadl_userdefineddatatype;
    }

}