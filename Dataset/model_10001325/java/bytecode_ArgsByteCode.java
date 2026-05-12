





import java.util.List;
import java.util.ArrayList;

public class bytecode_ArgsByteCode  {

    private int argCount;
    private String byteCode;



    public bytecode_ArgsByteCode(
        int argCount,        String byteCode    ) {
        this.argCount = argCount;
        this.byteCode = byteCode;
    }


    public int getArgcount() {
        return argCount;
    }

    public void setArgcount(int argCount) {
        this.argCount = argCount;
    }
    public String getBytecode() {
        return byteCode;
    }

    public void setBytecode(String byteCode) {
        this.byteCode = byteCode;
    }


}