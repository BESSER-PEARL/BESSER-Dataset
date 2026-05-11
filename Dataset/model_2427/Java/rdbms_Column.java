





import java.util.List;
import java.util.ArrayList;

public class rdbms_Column extends ModelElement {

    private int length;
    private String default;
    private int precision;
    private boolean nullable;





    private rdbms_ForeignKey rdbms_foreignkey;




    private rdbms_ForeignKey rdbms_foreignkey;


    public rdbms_Column(
        int length,        String default,        int precision,        boolean nullable    ) {
        super(
        );
        this.length = length;
        this.default = default;
        this.precision = precision;
        this.nullable = nullable;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }

    public rdbms_ForeignKey getRdbms_foreignkey() {
        return rdbms_foreignkey;
    }

    public void setRdbms_foreignkey(rdbms_ForeignKey rdbms_foreignkey) {
        this.rdbms_foreignkey = rdbms_foreignkey;
    }
    public rdbms_ForeignKey getRdbms_foreignkey() {
        return rdbms_foreignkey;
    }

    public void setRdbms_foreignkey(rdbms_ForeignKey rdbms_foreignkey) {
        this.rdbms_foreignkey = rdbms_foreignkey;
    }

}