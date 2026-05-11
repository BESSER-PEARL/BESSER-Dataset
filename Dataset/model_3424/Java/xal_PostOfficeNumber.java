





import java.util.List;
import java.util.ArrayList;

public class xal_PostOfficeNumber  {

    private String code;
    private String anyAttribute;
    private String indicator;
    private String mixed;
    private String indicatorOccurrence;



    public xal_PostOfficeNumber(
        String code,        String anyAttribute,        String indicator,        String mixed,        String indicatorOccurrence    ) {
        this.code = code;
        this.anyAttribute = anyAttribute;
        this.indicator = indicator;
        this.mixed = mixed;
        this.indicatorOccurrence = indicatorOccurrence;
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
    public String getIndicator() {
        return indicator;
    }

    public void setIndicator(String indicator) {
        this.indicator = indicator;
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


}