





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_Table  {






    private SpreadsheetMLSimplified_Column spreadsheetmlsimplified_column;




    private SpreadsheetMLSimplified_Row spreadsheetmlsimplified_row;




    private SpreadsheetMLSimplified_Worksheet spreadsheetmlsimplified_worksheet;




    private List<SpreadsheetMLSimplified_Column> spreadsheetmlsimplified_columns;




    private List<SpreadsheetMLSimplified_Row> spreadsheetmlsimplified_rows;




    private SpreadsheetMLSimplified_Worksheet spreadsheetmlsimplified_worksheet;


    public SpreadsheetMLSimplified_Table(
    ) {
        this.spreadsheetmlsimplified_columns = new ArrayList<>();
        this.spreadsheetmlsimplified_rows = new ArrayList<>();
    }

    public SpreadsheetMLSimplified_Table(
        ArrayList<SpreadsheetMLSimplified_Column> spreadsheetmlsimplified_columns,        ArrayList<SpreadsheetMLSimplified_Row> spreadsheetmlsimplified_rows    ) {
        this.spreadsheetmlsimplified_columns = spreadsheetmlsimplified_columns;
        this.spreadsheetmlsimplified_rows = spreadsheetmlsimplified_rows;
    }


    public SpreadsheetMLSimplified_Column getSpreadsheetmlsimplified_column() {
        return spreadsheetmlsimplified_column;
    }

    public void setSpreadsheetmlsimplified_column(SpreadsheetMLSimplified_Column spreadsheetmlsimplified_column) {
        this.spreadsheetmlsimplified_column = spreadsheetmlsimplified_column;
    }
    public SpreadsheetMLSimplified_Row getSpreadsheetmlsimplified_row() {
        return spreadsheetmlsimplified_row;
    }

    public void setSpreadsheetmlsimplified_row(SpreadsheetMLSimplified_Row spreadsheetmlsimplified_row) {
        this.spreadsheetmlsimplified_row = spreadsheetmlsimplified_row;
    }
    public SpreadsheetMLSimplified_Worksheet getSpreadsheetmlsimplified_worksheet() {
        return spreadsheetmlsimplified_worksheet;
    }

    public void setSpreadsheetmlsimplified_worksheet(SpreadsheetMLSimplified_Worksheet spreadsheetmlsimplified_worksheet) {
        this.spreadsheetmlsimplified_worksheet = spreadsheetmlsimplified_worksheet;
    }
    public List<SpreadsheetMLSimplified_Column> getSpreadsheetmlsimplified_columns() {
        return spreadsheetmlsimplified_columns;
    }

    public void addSpreadsheetmlsimplified_column(Spreadsheetmlsimplified_column spreadsheetmlsimplified_column) {
        this.spreadsheetmlsimplified_columns.add(spreadsheetmlsimplified_column);
    }
    public List<SpreadsheetMLSimplified_Row> getSpreadsheetmlsimplified_rows() {
        return spreadsheetmlsimplified_rows;
    }

    public void addSpreadsheetmlsimplified_row(Spreadsheetmlsimplified_row spreadsheetmlsimplified_row) {
        this.spreadsheetmlsimplified_rows.add(spreadsheetmlsimplified_row);
    }
    public SpreadsheetMLSimplified_Worksheet getSpreadsheetmlsimplified_worksheet() {
        return spreadsheetmlsimplified_worksheet;
    }

    public void setSpreadsheetmlsimplified_worksheet(SpreadsheetMLSimplified_Worksheet spreadsheetmlsimplified_worksheet) {
        this.spreadsheetmlsimplified_worksheet = spreadsheetmlsimplified_worksheet;
    }

}