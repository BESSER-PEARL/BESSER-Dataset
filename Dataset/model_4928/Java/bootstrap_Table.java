





import java.util.List;
import java.util.ArrayList;

public class bootstrap_Table extends Widget {

    private boolean striped;
    private String columnNames;
    private String rowNames;
    private boolean bordered;



    public bootstrap_Table(
        boolean striped,        String columnNames,        String rowNames,        boolean bordered    ) {
        super(
        );
        this.striped = striped;
        this.columnNames = columnNames;
        this.rowNames = rowNames;
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
    public boolean getBordered() {
        return bordered;
    }

    public void setBordered(boolean bordered) {
        this.bordered = bordered;
    }


}