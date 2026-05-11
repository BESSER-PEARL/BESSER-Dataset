





import java.util.List;
import java.util.ArrayList;

public class rdb_datatypes_DataType extends NamedElement {

    private String default;
    private String var;
    private boolean nullable;
    private int decimalDigits;
    private String check;
    private int size;



    public rdb_datatypes_DataType(
        String default,        String var,        boolean nullable,        int decimalDigits,        String check,        int size    ) {
        super(
        );
        this.default = default;
        this.var = var;
        this.nullable = nullable;
        this.decimalDigits = decimalDigits;
        this.check = check;
        this.size = size;
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
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}