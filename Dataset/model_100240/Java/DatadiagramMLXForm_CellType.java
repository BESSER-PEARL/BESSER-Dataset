





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_CellType  {

    private String err;
    private String formula;
    private String unit;
    private String value;



    public DatadiagramMLXForm_CellType(
        String err,        String formula,        String unit,        String value    ) {
        this.err = err;
        this.formula = formula;
        this.unit = unit;
        this.value = value;
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
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}