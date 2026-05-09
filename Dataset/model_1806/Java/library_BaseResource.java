





import java.util.List;
import java.util.ArrayList;

public class library_BaseResource extends Base {

    private String detailDisplay;
    private String expressionName;
    private String summaryDisplay;
    private String shortName;
    private String longName;



    public library_BaseResource(
        String detailDisplay,        String expressionName,        String summaryDisplay,        String shortName,        String longName    ) {
        super(
        );
        this.detailDisplay = detailDisplay;
        this.expressionName = expressionName;
        this.summaryDisplay = summaryDisplay;
        this.shortName = shortName;
        this.longName = longName;
    }


    public String getDetaildisplay() {
        return detailDisplay;
    }

    public void setDetaildisplay(String detailDisplay) {
        this.detailDisplay = detailDisplay;
    }
    public String getExpressionname() {
        return expressionName;
    }

    public void setExpressionname(String expressionName) {
        this.expressionName = expressionName;
    }
    public String getSummarydisplay() {
        return summaryDisplay;
    }

    public void setSummarydisplay(String summaryDisplay) {
        this.summaryDisplay = summaryDisplay;
    }
    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }
    public String getLongname() {
        return longName;
    }

    public void setLongname(String longName) {
        this.longName = longName;
    }


}