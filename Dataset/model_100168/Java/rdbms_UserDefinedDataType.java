





import java.util.List;
import java.util.ArrayList;

public class rdbms_UserDefinedDataType extends DataType {

    private int precision;
    private String defaultValue;
    private int length;





    private rdbms_Database rdbms_database;


    public rdbms_UserDefinedDataType(
        int precision,        String defaultValue,        int length    ) {
        super(
        );
        this.precision = precision;
        this.defaultValue = defaultValue;
        this.length = length;
    }


    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public rdbms_Database getRdbms_database() {
        return rdbms_database;
    }

    public void setRdbms_database(rdbms_Database rdbms_database) {
        this.rdbms_database = rdbms_database;
    }

}