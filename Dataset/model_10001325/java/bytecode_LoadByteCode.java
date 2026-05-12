





import java.util.List;
import java.util.ArrayList;

public class bytecode_LoadByteCode  {

    private String byteCode;
    private int loadOffset;
    private String loadID;



    public bytecode_LoadByteCode(
        String byteCode,        int loadOffset,        String loadID    ) {
        this.byteCode = byteCode;
        this.loadOffset = loadOffset;
        this.loadID = loadID;
    }


    public String getBytecode() {
        return byteCode;
    }

    public void setBytecode(String byteCode) {
        this.byteCode = byteCode;
    }
    public int getLoadoffset() {
        return loadOffset;
    }

    public void setLoadoffset(int loadOffset) {
        this.loadOffset = loadOffset;
    }
    public String getLoadid() {
        return loadID;
    }

    public void setLoadid(String loadID) {
        this.loadID = loadID;
    }


}