





import java.util.List;
import java.util.ArrayList;

public class library_BaseResource extends Base {

    private String longName;
    private String expressionName;
    private String shortName;
    private String summaryDisplay;
    private String detailDisplay;



    public library_BaseResource(
        String longName,        String expressionName,        String shortName,        String summaryDisplay,        String detailDisplay    ) {
        super(
        );
        this.longName = longName;
        this.expressionName = expressionName;
        this.shortName = shortName;
        this.summaryDisplay = summaryDisplay;
        this.detailDisplay = detailDisplay;
    }


    public String getLongname() {
        return longName;
    }

    public void setLongname(String longName) {
        this.longName = longName;
    }
    public String getExpressionname() {
        return expressionName;
    }

    public void setExpressionname(String expressionName) {
        this.expressionName = expressionName;
    }
    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }
    public String getSummarydisplay() {
        return summaryDisplay;
    }

    public void setSummarydisplay(String summaryDisplay) {
        this.summaryDisplay = summaryDisplay;
    }
    public String getDetaildisplay() {
        return detailDisplay;
    }

    public void setDetaildisplay(String detailDisplay) {
        this.detailDisplay = detailDisplay;
    }


}