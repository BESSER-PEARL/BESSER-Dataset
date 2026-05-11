





import java.util.List;
import java.util.ArrayList;

public class xal_SubPremiseName  {

    private String mixed;
    private String typeOccurrence;
    private String type;
    private String code;
    private String anyAttribute;





    private xal_SubPremise xal_subpremise;


    public xal_SubPremiseName(
        String mixed,        String typeOccurrence,        String type,        String code,        String anyAttribute    ) {
        this.mixed = mixed;
        this.typeOccurrence = typeOccurrence;
        this.type = type;
        this.code = code;
        this.anyAttribute = anyAttribute;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getTypeoccurrence() {
        return typeOccurrence;
    }

    public void setTypeoccurrence(String typeOccurrence) {
        this.typeOccurrence = typeOccurrence;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }

    public xal_SubPremise getXal_subpremise() {
        return xal_subpremise;
    }

    public void setXal_subpremise(xal_SubPremise xal_subpremise) {
        this.xal_subpremise = xal_subpremise;
    }

}