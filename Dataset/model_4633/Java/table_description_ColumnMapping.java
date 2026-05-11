





import java.util.List;
import java.util.ArrayList;

public class table_description_ColumnMapping extends TableMapping {

    private String headerLabelExpression;
    private int initialWidth;



    public table_description_ColumnMapping(
        String headerLabelExpression,        int initialWidth    ) {
        super(
        );
        this.headerLabelExpression = headerLabelExpression;
        this.initialWidth = initialWidth;
    }


    public String getHeaderlabelexpression() {
        return headerLabelExpression;
    }

    public void setHeaderlabelexpression(String headerLabelExpression) {
        this.headerLabelExpression = headerLabelExpression;
    }
    public int getInitialwidth() {
        return initialWidth;
    }

    public void setInitialwidth(int initialWidth) {
        this.initialWidth = initialWidth;
    }


}