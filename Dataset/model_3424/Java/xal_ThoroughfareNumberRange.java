





import java.util.List;
import java.util.ArrayList;

public class xal_ThoroughfareNumberRange  {

    private String code;
    private String numberRangeOccurrence;
    private String separator;
    private String indicator;
    private String type;
    private String anyAttribute;
    private String indicatorOccurrence;
    private String rangeType;



    public xal_ThoroughfareNumberRange(
        String code,        String numberRangeOccurrence,        String separator,        String indicator,        String type,        String anyAttribute,        String indicatorOccurrence,        String rangeType    ) {
        this.code = code;
        this.numberRangeOccurrence = numberRangeOccurrence;
        this.separator = separator;
        this.indicator = indicator;
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.indicatorOccurrence = indicatorOccurrence;
        this.rangeType = rangeType;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getNumberrangeoccurrence() {
        return numberRangeOccurrence;
    }

    public void setNumberrangeoccurrence(String numberRangeOccurrence) {
        this.numberRangeOccurrence = numberRangeOccurrence;
    }
    public String getSeparator() {
        return separator;
    }

    public void setSeparator(String separator) {
        this.separator = separator;
    }
    public String getIndicator() {
        return indicator;
    }

    public void setIndicator(String indicator) {
        this.indicator = indicator;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getIndicatoroccurrence() {
        return indicatorOccurrence;
    }

    public void setIndicatoroccurrence(String indicatorOccurrence) {
        this.indicatorOccurrence = indicatorOccurrence;
    }
    public String getRangetype() {
        return rangeType;
    }

    public void setRangetype(String rangeType) {
        this.rangeType = rangeType;
    }


}