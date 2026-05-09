





import java.util.List;
import java.util.ArrayList;

public class eTJ_HideJournalEntry extends ReportAttribute, IcalReportAttribute {

    private String expression;



    public eTJ_HideJournalEntry(
        String expression    ) {
        super(
        );
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }


}