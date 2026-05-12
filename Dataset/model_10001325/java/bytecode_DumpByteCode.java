





import java.util.List;
import java.util.ArrayList;

public class bytecode_DumpByteCode  {

    private String theArg;
    private String byteCode;



    public bytecode_DumpByteCode(
        String theArg,        String byteCode    ) {
        this.theArg = theArg;
        this.byteCode = byteCode;
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