





import java.util.List;
import java.util.ArrayList;

public class sql_from_TableExpression  {

    private String label;





    private from_Table from_table;


    public sql_from_TableExpression(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public from_Table getFrom_table() {
        return from_table;
    }

    public void setFrom_table(from_Table from_table) {
        this.from_table = from_table;
    }

}