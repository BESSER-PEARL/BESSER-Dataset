





import java.util.List;
import java.util.ArrayList;

public class bytecode_CallByteCode  {

    private int lineNO;
    private String theArg;
    private String byteCode;



    public bytecode_CallByteCode(
        int lineNO,        String theArg,        String byteCode    ) {
        this.lineNO = lineNO;
        this.theArg = theArg;
        this.byteCode = byteCode;
    }


    public int getLineno() {
        return lineNO;
    }

    public void setLineno(int lineNO) {
        this.lineNO = lineNO;
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


}