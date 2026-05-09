





import java.util.List;
import java.util.ArrayList;

public class library_BaseResource extends Base {

    private String detailDisplay;
    private String longName;
    private String summaryDisplay;
    private String expressionName;
    private String shortName;



    public library_BaseResource(
        String detailDisplay,        String longName,        String summaryDisplay,        String expressionName,        String shortName    ) {
        super(
        );
        this.detailDisplay = detailDisplay;
        this.longName = longName;
        this.summaryDisplay = summaryDisplay;
        this.expressionName = expressionName;
        this.shortName = shortName;
    }


    public String getDetaildisplay() {
        return detailDisplay;
    }

    public void setDetaildisplay(String detailDisplay) {
        this.detailDisplay = detailDisplay;
    }
    public String getLongname() {
        return longName;
    }

    public void setLongname(String longName) {
        this.longName = longName;
    }
    public String getSummarydisplay() {
        return summaryDisplay;
    }

    public void setSummarydisplay(String summaryDisplay) {
        this.summaryDisplay = summaryDisplay;
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


}