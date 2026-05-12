





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_Table  {






    private List<Row> rows;




    private Worksheet worksheet;


    public SpreadsheetMLSimplified_Table(
    ) {
        this.rows = new ArrayList<>();
    }

    public SpreadsheetMLSimplified_Table(
        ArrayList<Row> rows    ) {
        this.rows = rows;
    }


    public List<Row> getRows() {
        return rows;
    }

    public void addRow(Row row) {
        this.rows.add(row);
    }
    public Worksheet getWorksheet() {
        return worksheet;
    }

    public void setWorksheet(Worksheet worksheet) {
        this.worksheet = worksheet;
    }

}