





import java.util.List;
import java.util.ArrayList;

public class webapp_Table extends Widget {

    private String rowNames;
    private boolean striped;
    private String columnNames;
    private boolean bordered;



    public webapp_Table(
        String rowNames,        boolean striped,        String columnNames,        boolean bordered    ) {
        super(
        );
        this.rowNames = rowNames;
        this.striped = striped;
        this.columnNames = columnNames;
        this.bordered = bordered;
    }


    public String getRownames() {
        return rowNames;
    }

    public void setRownames(String rowNames) {
        this.rowNames = rowNames;
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
    public boolean getBordered() {
        return bordered;
    }

    public void setBordered(boolean bordered) {
        this.bordered = bordered;
    }


}