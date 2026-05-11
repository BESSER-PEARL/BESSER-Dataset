





import java.util.List;
import java.util.ArrayList;

public class rdbmdl_datatypes_DataType extends NamedElement {

    private int decimalDigits;
    private int size;
    private String check;
    private String default;
    private String var;
    private boolean nullable;



    public rdbmdl_datatypes_DataType(
        int decimalDigits,        int size,        String check,        String default,        String var,        boolean nullable    ) {
        super(
        );
        this.decimalDigits = decimalDigits;
        this.size = size;
        this.check = check;
        this.default = default;
        this.var = var;
        this.nullable = nullable;
    }


    public int getDecimaldigits() {
        return decimalDigits;
    }

    public void setDecimaldigits(int decimalDigits) {
        this.decimalDigits = decimalDigits;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getCheck() {
        return check;
    }

    public void setCheck(String check) {
        this.check = check;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }


}