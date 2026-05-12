





import java.util.List;
import java.util.ArrayList;

public class bytecode_GoToByteCode  {

    private String theArg;
    private int lineNO;
    private String byteCode;



    public bytecode_GoToByteCode(
        String theArg,        int lineNO,        String byteCode    ) {
        this.theArg = theArg;
        this.lineNO = lineNO;
        this.byteCode = byteCode;
    }


    public String getThearg() {
        return theArg;
    }

    public void setThearg(String theArg) {
        this.theArg = theArg;
    }
    public int getLineno() {
        return lineNO;
    }

    public void setLineno(int lineNO) {
        this.lineNO = lineNO;
    }
    public String getBytecode() {
        return byteCode;
    }

    public void setBytecode(String byteCode) {
        this.byteCode = byteCode;
    }


}