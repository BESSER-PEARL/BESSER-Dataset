





import java.util.List;
import java.util.ArrayList;

public class bootstrap_Table extends Widget {

    private boolean bordered;
    private boolean striped;
    private String columnNames;
    private String rowNames;



    public bootstrap_Table(
        boolean bordered,        boolean striped,        String columnNames,        String rowNames    ) {
        super(
        );
        this.bordered = bordered;
        this.striped = striped;
        this.columnNames = columnNames;
        this.rowNames = rowNames;
    }


    public boolean getBordered() {
        return bordered;
    }

    public void setBordered(boolean bordered) {
        this.bordered = bordered;
    }
    public boolean getStriped() {
        return striped;
    }

    public void setStriped(boolean striped) {
        this.striped = striped;
    }
    public String getColumnnames() {
        return columnNames;
    }

    public void setColumnnames(String columnNames) {
        this.columnNames = columnNames;
    }
    public String getRownames() {
        return rowNames;
    }

    public void setRownames(String rowNames) {
        this.rowNames = rowNames;
    }


}