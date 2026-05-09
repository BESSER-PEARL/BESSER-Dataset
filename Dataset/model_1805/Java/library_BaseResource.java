





import java.util.List;
import java.util.ArrayList;

public class library_BaseResource extends Base {

    private String expressionName;
    private String detailDisplay;
    private String summaryDisplay;
    private String longName;
    private String shortName;



    public library_BaseResource(
        String expressionName,        String detailDisplay,        String summaryDisplay,        String longName,        String shortName    ) {
        super(
        );
        this.expressionName = expressionName;
        this.detailDisplay = detailDisplay;
        this.summaryDisplay = summaryDisplay;
        this.longName = longName;
        this.shortName = shortName;
    }


    public String getExpressionname() {
        return expressionName;
    }

    public void setExpressionname(String expressionName) {
        this.expressionName = expressionName;
    }
    public String getDetaildisplay() {
        return detailDisplay;
    }

    public void setDetaildisplay(String detailDisplay) {
        this.detailDisplay = detailDisplay;
    }
    public String getSummarydisplay() {
        return summaryDisplay;
    }

    public void setSummarydisplay(String summaryDisplay) {
        this.summaryDisplay = summaryDisplay;
    }
    public String getLongname() {
        return longName;
    }

    public void setLongname(String longName) {
        this.longName = longName;
    }
    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }


}