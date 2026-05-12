





import java.util.List;
import java.util.ArrayList;

public class spreadsheet_Cell  {

    private String StringValue;
    private String ValueFormatted;
    private String CellType;
    private float DoubleValue;



    public spreadsheet_Cell(
        String StringValue,        String ValueFormatted,        String CellType,        float DoubleValue    ) {
        this.StringValue = StringValue;
        this.ValueFormatted = ValueFormatted;
        this.CellType = CellType;
        this.DoubleValue = DoubleValue;
    }


    public String getStringvalue() {
        return StringValue;
    }

    public void setStringvalue(String StringValue) {
        this.StringValue = StringValue;
    }
    public String getValueformatted() {
        return ValueFormatted;
    }

    public void setValueformatted(String ValueFormatted) {
        this.ValueFormatted = ValueFormatted;
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


}