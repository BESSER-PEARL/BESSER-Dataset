





import java.util.List;
import java.util.ArrayList;

public class xal_ThoroughfareNumber  {

    private String code;
    private String numberType;
    private String numberOccurrence;
    private String indicatorOccurrence;
    private String anyAttribute;
    private String type;
    private String mixed;
    private String indicator;





    private xal_ThoroughfareNumberTo xal_thoroughfarenumberto;




    private xal_DocumentRoot xal_documentroot;




    private xal_Thoroughfare xal_thoroughfare;




    private xal_ThoroughfareNumberFrom xal_thoroughfarenumberfrom;


    public xal_ThoroughfareNumber(
        String code,        String numberType,        String numberOccurrence,        String indicatorOccurrence,        String anyAttribute,        String type,        String mixed,        String indicator    ) {
        this.code = code;
        this.numberType = numberType;
        this.numberOccurrence = numberOccurrence;
        this.indicatorOccurrence = indicatorOccurrence;
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.mixed = mixed;
        this.indicator = indicator;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getNumbertype() {
        return numberType;
    }

    public void setNumbertype(String numberType) {
        this.numberType = numberType;
    }
    public String getNumberoccurrence() {
        return numberOccurrence;
    }

    public void setNumberoccurrence(String numberOccurrence) {
        this.numberOccurrence = numberOccurrence;
    }
    public String getIndicatoroccurrence() {
        return indicatorOccurrence;
    }

    public void setIndicatoroccurrence(String indicatorOccurrence) {
        this.indicatorOccurrence = indicatorOccurrence;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
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
    public String getIndicator() {
        return indicator;
    }

    public void setIndicator(String indicator) {
        this.indicator = indicator;
    }

    public xal_ThoroughfareNumberTo getXal_thoroughfarenumberto() {
        return xal_thoroughfarenumberto;
    }

    public void setXal_thoroughfarenumberto(xal_ThoroughfareNumberTo xal_thoroughfarenumberto) {
        this.xal_thoroughfarenumberto = xal_thoroughfarenumberto;
    }
    public xal_DocumentRoot getXal_documentroot() {
        return xal_documentroot;
    }

    public void setXal_documentroot(xal_DocumentRoot xal_documentroot) {
        this.xal_documentroot = xal_documentroot;
    }
    public xal_Thoroughfare getXal_thoroughfare() {
        return xal_thoroughfare;
    }

    public void setXal_thoroughfare(xal_Thoroughfare xal_thoroughfare) {
        this.xal_thoroughfare = xal_thoroughfare;
    }
    public xal_ThoroughfareNumberFrom getXal_thoroughfarenumberfrom() {
        return xal_thoroughfarenumberfrom;
    }

    public void setXal_thoroughfarenumberfrom(xal_ThoroughfareNumberFrom xal_thoroughfarenumberfrom) {
        this.xal_thoroughfarenumberfrom = xal_thoroughfarenumberfrom;
    }

}