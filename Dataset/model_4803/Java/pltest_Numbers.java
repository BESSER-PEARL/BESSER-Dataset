





import java.util.List;
import java.util.ArrayList;

public class pltest_Numbers  {

    private String bigDecimal;
    private float double;
    private float float;
    private String long;
    private int int;
    private String bigInt;



    public pltest_Numbers(
        String bigDecimal,        float double,        float float,        String long,        int int,        String bigInt    ) {
        this.bigDecimal = bigDecimal;
        this.double = double;
        this.float = float;
        this.long = long;
        this.int = int;
        this.bigInt = bigInt;
    }


    public String getBigdecimal() {
        return bigDecimal;
    }

    public void setBigdecimal(String bigDecimal) {
        this.bigDecimal = bigDecimal;
    }
    public float getDouble() {
        return double;
    }

    public void setDouble(float double) {
        this.double = double;
    }
    public float getFloat() {
        return float;
    }

    public void setFloat(float float) {
        this.float = float;
    }
    public String getLong() {
        return long;
    }

    public void setLong(String long) {
        this.long = long;
    }
    public int getInt() {
        return int;
    }

    public void setInt(int int) {
        this.int = int;
    }
    public String getBigint() {
        return bigInt;
    }

    public void setBigint(String bigInt) {
        this.bigInt = bigInt;
    }


}