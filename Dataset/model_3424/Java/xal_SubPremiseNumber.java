





import java.util.List;
import java.util.ArrayList;

public class xal_SubPremiseNumber  {

    private String code;
    private String premiseNumberSeparator;
    private String mixed;
    private String indicatorOccurrence;
    private String indicator;
    private String anyAttribute;
    private String type;
    private String numberTypeOccurrence;





    private xal_SubPremise xal_subpremise;


    public xal_SubPremiseNumber(
        String code,        String premiseNumberSeparator,        String mixed,        String indicatorOccurrence,        String indicator,        String anyAttribute,        String type,        String numberTypeOccurrence    ) {
        this.code = code;
        this.premiseNumberSeparator = premiseNumberSeparator;
        this.mixed = mixed;
        this.indicatorOccurrence = indicatorOccurrence;
        this.indicator = indicator;
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.numberTypeOccurrence = numberTypeOccurrence;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getPremisenumberseparator() {
        return premiseNumberSeparator;
    }

    public void setPremisenumberseparator(String premiseNumberSeparator) {
        this.premiseNumberSeparator = premiseNumberSeparator;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getIndicatoroccurrence() {
        return indicatorOccurrence;
    }

    public void setIndicatoroccurrence(String indicatorOccurrence) {
        this.indicatorOccurrence = indicatorOccurrence;
    }
    public String getIndicator() {
        return indicator;
    }

    public void setIndicator(String indicator) {
        this.indicator = indicator;
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
    public String getNumbertypeoccurrence() {
        return numberTypeOccurrence;
    }

    public void setNumbertypeoccurrence(String numberTypeOccurrence) {
        this.numberTypeOccurrence = numberTypeOccurrence;
    }

    public xal_SubPremise getXal_subpremise() {
        return xal_subpremise;
    }

    public void setXal_subpremise(xal_SubPremise xal_subpremise) {
        this.xal_subpremise = xal_subpremise;
    }

}