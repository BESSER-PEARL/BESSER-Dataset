





import java.util.List;
import java.util.ArrayList;

public class spreadsheet_Cell  {

    private String StringValue;
    private String CellType;
    private float DoubleValue;
    private String ValueFormatted;





    private spreadsheet_Row spreadsheet_row;




    private spreadsheet_Column spreadsheet_column;




    private spreadsheet_Row spreadsheet_row;




    private spreadsheet_Column spreadsheet_column;


    public spreadsheet_Cell(
        String StringValue,        String CellType,        float DoubleValue,        String ValueFormatted    ) {
        this.StringValue = StringValue;
        this.CellType = CellType;
        this.DoubleValue = DoubleValue;
        this.ValueFormatted = ValueFormatted;
    }


    public String getStringvalue() {
        return StringValue;
    }

    public void setStringvalue(String StringValue) {
        this.StringValue = StringValue;
    }
    public String getCelltype() {
        return CellType;
    }

    public void setCelltype(String CellType) {
        this.CellType = CellType;
    }
    public float getDoublevalue() {
        return DoubleValue;
    }

    public void setDoublevalue(float DoubleValue) {
        this.DoubleValue = DoubleValue;
    }
    public String getValueformatted() {
        return ValueFormatted;
    }

    public void setValueformatted(String ValueFormatted) {
        this.ValueFormatted = ValueFormatted;
    }

    public spreadsheet_Row getSpreadsheet_row() {
        return spreadsheet_row;
    }

    public void setSpreadsheet_row(spreadsheet_Row spreadsheet_row) {
        this.spreadsheet_row = spreadsheet_row;
    }
    public spreadsheet_Column getSpreadsheet_column() {
        return spreadsheet_column;
    }

    public void setSpreadsheet_column(spreadsheet_Column spreadsheet_column) {
        this.spreadsheet_column = spreadsheet_column;
    }
    public spreadsheet_Row getSpreadsheet_row() {
        return spreadsheet_row;
    }

    public void setSpreadsheet_row(spreadsheet_Row spreadsheet_row) {
        this.spreadsheet_row = spreadsheet_row;
    }
    public spreadsheet_Column getSpreadsheet_column() {
        return spreadsheet_column;
    }

    public void setSpreadsheet_column(spreadsheet_Column spreadsheet_column) {
        this.spreadsheet_column = spreadsheet_column;
    }

}