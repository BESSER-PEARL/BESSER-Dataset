





import java.util.List;
import java.util.ArrayList;

public class xal_PremiseNumberRange  {

    private String type;
    private String separator;
    private String indicator;
    private String rangeType;
    private String numberRangeOccurence;
    private String indicatorOccurence;



    public xal_PremiseNumberRange(
        String type,        String separator,        String indicator,        String rangeType,        String numberRangeOccurence,        String indicatorOccurence    ) {
        this.type = type;
        this.separator = separator;
        this.indicator = indicator;
        this.rangeType = rangeType;
        this.numberRangeOccurence = numberRangeOccurence;
        this.indicatorOccurence = indicatorOccurence;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public String getRangetype() {
        return rangeType;
    }

    public void setRangetype(String rangeType) {
        this.rangeType = rangeType;
    }
    public String getNumberrangeoccurence() {
        return numberRangeOccurence;
    }

    public void setNumberrangeoccurence(String numberRangeOccurence) {
        this.numberRangeOccurence = numberRangeOccurence;
    }
    public String getIndicatoroccurence() {
        return indicatorOccurence;
    }

    public void setIndicatoroccurence(String indicatorOccurence) {
        this.indicatorOccurence = indicatorOccurence;
    }


}