





import java.util.List;
import java.util.ArrayList;

public class bytecode_StoreByteCode  {

    private String storeID;
    private String theArg;
    private int storeValue;
    private String byteCode;



    public bytecode_StoreByteCode(
        String storeID,        String theArg,        int storeValue,        String byteCode    ) {
        this.storeID = storeID;
        this.theArg = theArg;
        this.storeValue = storeValue;
        this.byteCode = byteCode;
    }


    public String getStoreid() {
        return storeID;
    }

    public void setStoreid(String storeID) {
        this.storeID = storeID;
    }
    public String getThearg() {
        return theArg;
    }

    public void setThearg(String theArg) {
        this.theArg = theArg;
    }
    public int getStorevalue() {
        return storeValue;
    }

    public void setStorevalue(int storeValue) {
        this.storeValue = storeValue;
    }
    public String getBytecode() {
        return byteCode;
    }

    public void setBytecode(String byteCode) {
        this.byteCode = byteCode;
    }


}