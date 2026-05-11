





import java.util.List;
import java.util.ArrayList;

public class xal_DependentLocalityNumber  {

    private String anyAttribute;
    private String mixed;
    private String code;
    private String nameNumberOccurrence;





    private xal_DependentLocality xal_dependentlocality;


    public xal_DependentLocalityNumber(
        String anyAttribute,        String mixed,        String code,        String nameNumberOccurrence    ) {
        this.anyAttribute = anyAttribute;
        this.mixed = mixed;
        this.code = code;
        this.nameNumberOccurrence = nameNumberOccurrence;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getNamenumberoccurrence() {
        return nameNumberOccurrence;
    }

    public void setNamenumberoccurrence(String nameNumberOccurrence) {
        this.nameNumberOccurrence = nameNumberOccurrence;
    }

    public xal_DependentLocality getXal_dependentlocality() {
        return xal_dependentlocality;
    }

    public void setXal_dependentlocality(xal_DependentLocality xal_dependentlocality) {
        this.xal_dependentlocality = xal_dependentlocality;
    }

}