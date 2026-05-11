





import java.util.List;
import java.util.ArrayList;

public class xal_BuildingName  {

    private String anyAttribute;
    private String code;
    private String typeOccurrence;
    private String mixed;
    private String type;





    private xal_SubPremise xal_subpremise;


    public xal_BuildingName(
        String anyAttribute,        String code,        String typeOccurrence,        String mixed,        String type    ) {
        this.anyAttribute = anyAttribute;
        this.code = code;
        this.typeOccurrence = typeOccurrence;
        this.mixed = mixed;
        this.type = type;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getTypeoccurrence() {
        return typeOccurrence;
    }

    public void setTypeoccurrence(String typeOccurrence) {
        this.typeOccurrence = typeOccurrence;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xal_SubPremise getXal_subpremise() {
        return xal_subpremise;
    }

    public void setXal_subpremise(xal_SubPremise xal_subpremise) {
        this.xal_subpremise = xal_subpremise;
    }

}