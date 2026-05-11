





import java.util.List;
import java.util.ArrayList;

public class xal_ThoroughfareNumberPrefix  {

    private String anyAttribute;
    private String numberPrefixSeparator;
    private String code;
    private String type;
    private String mixed;





    private xal_ThoroughfareNumberFrom xal_thoroughfarenumberfrom;




    private xal_DocumentRoot xal_documentroot;




    private xal_ThoroughfareNumberTo xal_thoroughfarenumberto;




    private xal_Thoroughfare xal_thoroughfare;


    public xal_ThoroughfareNumberPrefix(
        String anyAttribute,        String numberPrefixSeparator,        String code,        String type,        String mixed    ) {
        this.anyAttribute = anyAttribute;
        this.numberPrefixSeparator = numberPrefixSeparator;
        this.code = code;
        this.type = type;
        this.mixed = mixed;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getNumberprefixseparator() {
        return numberPrefixSeparator;
    }

    public void setNumberprefixseparator(String numberPrefixSeparator) {
        this.numberPrefixSeparator = numberPrefixSeparator;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public xal_ThoroughfareNumberFrom getXal_thoroughfarenumberfrom() {
        return xal_thoroughfarenumberfrom;
    }

    public void setXal_thoroughfarenumberfrom(xal_ThoroughfareNumberFrom xal_thoroughfarenumberfrom) {
        this.xal_thoroughfarenumberfrom = xal_thoroughfarenumberfrom;
    }
    public xal_DocumentRoot getXal_documentroot() {
        return xal_documentroot;
    }

    public void setXal_documentroot(xal_DocumentRoot xal_documentroot) {
        this.xal_documentroot = xal_documentroot;
    }
    public xal_ThoroughfareNumberTo getXal_thoroughfarenumberto() {
        return xal_thoroughfarenumberto;
    }

    public void setXal_thoroughfarenumberto(xal_ThoroughfareNumberTo xal_thoroughfarenumberto) {
        this.xal_thoroughfarenumberto = xal_thoroughfarenumberto;
    }
    public xal_Thoroughfare getXal_thoroughfare() {
        return xal_thoroughfare;
    }

    public void setXal_thoroughfare(xal_Thoroughfare xal_thoroughfare) {
        this.xal_thoroughfare = xal_thoroughfare;
    }

}