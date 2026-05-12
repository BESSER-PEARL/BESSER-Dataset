





import java.util.List;
import java.util.ArrayList;

public class bytecode_PopByteCode  {

    private String theArg;
    private String byteCode;
    private int count;



    public bytecode_PopByteCode(
        String theArg,        String byteCode,        int count    ) {
        this.theArg = theArg;
        this.byteCode = byteCode;
        this.count = count;
    }


    public String getThearg() {
        return theArg;
    }

    public void setThearg(String theArg) {
        this.theArg = theArg;
    }
    public String getBytecode() {
        return byteCode;
    }

    public void setBytecode(String byteCode) {
        this.byteCode = byteCode;
    }
    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }


}