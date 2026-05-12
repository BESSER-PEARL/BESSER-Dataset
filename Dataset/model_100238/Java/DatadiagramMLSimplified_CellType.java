





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLSimplified_CellType  {

    private String err;
    private String formula;
    private String value;
    private String unit;



    public DatadiagramMLSimplified_CellType(
        String err,        String formula,        String value,        String unit    ) {
        this.err = err;
        this.formula = formula;
        this.value = value;
        this.unit = unit;
    }


    public String getErr() {
        return err;
    }

    public void setErr(String err) {
        this.err = err;
    }
    public String getFormula() {
        return formula;
    }

    public void setFormula(String formula) {
        this.formula = formula;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}