





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_CellType  {

    private String value;
    private String err;
    private String unit;
    private String formula;



    public DatadiagramMLTextFormat_CellType(
        String value,        String err,        String unit,        String formula    ) {
        this.value = value;
        this.err = err;
        this.unit = unit;
        this.formula = formula;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getErr() {
        return err;
    }

    public void setErr(String err) {
        this.err = err;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getFormula() {
        return formula;
    }

    public void setFormula(String formula) {
        this.formula = formula;
    }


}