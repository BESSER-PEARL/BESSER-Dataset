





import java.util.List;
import java.util.ArrayList;

public class bytecode_LitByteCode  {

    private String byteCode;
    private int litValue;
    private String litID;



    public bytecode_LitByteCode(
        String byteCode,        int litValue,        String litID    ) {
        this.byteCode = byteCode;
        this.litValue = litValue;
        this.litID = litID;
    }


    public String getBytecode() {
        return byteCode;
    }

    public void setBytecode(String byteCode) {
        this.byteCode = byteCode;
    }
    public int getLitvalue() {
        return litValue;
    }

    public void setLitvalue(int litValue) {
        this.litValue = litValue;
    }
    public String getLitid() {
        return litID;
    }

    public void setLitid(String litID) {
        this.litID = litID;
    }


}