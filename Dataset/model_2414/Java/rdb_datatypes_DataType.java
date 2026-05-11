





import java.util.List;
import java.util.ArrayList;

public class rdb_datatypes_DataType extends NamedElement {

    private boolean nullable;
    private int decimalDigits;
    private String check;
    private String var;
    private int size;
    private String default;



    public rdb_datatypes_DataType(
        boolean nullable,        int decimalDigits,        String check,        String var,        int size,        String default    ) {
        super(
        );
        this.nullable = nullable;
        this.decimalDigits = decimalDigits;
        this.check = check;
        this.var = var;
        this.size = size;
        this.default = default;
    }


    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public int getDecimaldigits() {
        return decimalDigits;
    }

    public void setDecimaldigits(int decimalDigits) {
        this.decimalDigits = decimalDigits;
    }
    public String getCheck() {
        return check;
    }

    public void setCheck(String check) {
        this.check = check;
    }
    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }


}