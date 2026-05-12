





import java.util.List;
import java.util.ArrayList;

public class rdbms_Column extends ModelElement {

    private boolean nullable;
    private String default;
    private int precision;
    private int length;





    private rdbms_DataType rdbms_datatype;




    private rdbms_Table rdbms_table;


    public rdbms_Column(
        boolean nullable,        String default,        int precision,        int length    ) {
        super(
        );
        this.nullable = nullable;
        this.default = default;
        this.precision = precision;
        this.length = length;
    }


    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
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
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public rdbms_DataType getRdbms_datatype() {
        return rdbms_datatype;
    }

    public void setRdbms_datatype(rdbms_DataType rdbms_datatype) {
        this.rdbms_datatype = rdbms_datatype;
    }
    public rdbms_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(rdbms_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }

}