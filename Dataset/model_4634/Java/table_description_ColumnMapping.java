





import java.util.List;
import java.util.ArrayList;

public class table_description_ColumnMapping extends TableMapping {

    private int initialWidth;
    private String headerLabelExpression;



    public table_description_ColumnMapping(
        int initialWidth,        String headerLabelExpression    ) {
        super(
        );
        this.initialWidth = initialWidth;
        this.headerLabelExpression = headerLabelExpression;
    }


    public int getInitialwidth() {
        return initialWidth;
    }

    public void setInitialwidth(int initialWidth) {
        this.initialWidth = initialWidth;
    }
    public String getHeaderlabelexpression() {
        return headerLabelExpression;
    }

    public void setHeaderlabelexpression(String headerLabelExpression) {
        this.headerLabelExpression = headerLabelExpression;
    }


}