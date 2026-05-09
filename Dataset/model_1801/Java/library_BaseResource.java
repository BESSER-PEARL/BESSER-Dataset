





import java.util.List;
import java.util.ArrayList;

public class library_BaseResource extends Base {

    private String expressionName;
    private String detailDisplay;
    private String longName;
    private String shortName;
    private String summaryDisplay;





    private library_ExpressionResult library_expressionresult;


    public library_BaseResource(
        String expressionName,        String detailDisplay,        String longName,        String shortName,        String summaryDisplay    ) {
        super(
        );
        this.expressionName = expressionName;
        this.detailDisplay = detailDisplay;
        this.longName = longName;
        this.shortName = shortName;
        this.summaryDisplay = summaryDisplay;
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
    public String getSummarydisplay() {
        return summaryDisplay;
    }

    public void setSummarydisplay(String summaryDisplay) {
        this.summaryDisplay = summaryDisplay;
    }

    public library_ExpressionResult getLibrary_expressionresult() {
        return library_expressionresult;
    }

    public void setLibrary_expressionresult(library_ExpressionResult library_expressionresult) {
        this.library_expressionresult = library_expressionresult;
    }

}