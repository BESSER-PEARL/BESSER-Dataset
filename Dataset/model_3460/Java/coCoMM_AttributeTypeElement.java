





import java.util.List;
import java.util.ArrayList;

public class coCoMM_AttributeTypeElement  {

    private String name;
    private String dataType;





    private coCoMM_AttributeType cocomm_attributetype;


    public coCoMM_AttributeTypeElement(
        String name,        String dataType    ) {
        this.name = name;
        this.dataType = dataType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }

    public coCoMM_AttributeType getCocomm_attributetype() {
        return cocomm_attributetype;
    }

    public void setCocomm_attributetype(coCoMM_AttributeType cocomm_attributetype) {
        this.cocomm_attributetype = cocomm_attributetype;
    }

}