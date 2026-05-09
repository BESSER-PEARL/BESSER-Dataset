





import java.util.List;
import java.util.ArrayList;

public class project_HideJournalEntry extends IcalReportAttribute, ReportAttribute {

    private String expression;



    public project_HideJournalEntry(
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