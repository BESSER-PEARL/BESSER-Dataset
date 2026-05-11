





import java.util.List;
import java.util.ArrayList;

public class afpText_CPC extends structuredField {

    private String VSFlags;
    private String VSCharSN;
    private String DefCharID;
    private String CPIRGLen;
    private String PrtFlags;
    private String VSChar;



    public afpText_CPC(
        String VSFlags,        String VSCharSN,        String DefCharID,        String CPIRGLen,        String PrtFlags,        String VSChar    ) {
        super(
        );
        this.VSFlags = VSFlags;
        this.VSCharSN = VSCharSN;
        this.DefCharID = DefCharID;
        this.CPIRGLen = CPIRGLen;
        this.PrtFlags = PrtFlags;
        this.VSChar = VSChar;
    }


    public String getVsflags() {
        return VSFlags;
    }

    public void setVsflags(String VSFlags) {
        this.VSFlags = VSFlags;
    }
    public String getVscharsn() {
        return VSCharSN;
    }

    public void setVscharsn(String VSCharSN) {
        this.VSCharSN = VSCharSN;
    }
    public String getDefcharid() {
        return DefCharID;
    }

    public void setDefcharid(String DefCharID) {
        this.DefCharID = DefCharID;
    }
    public String getCpirglen() {
        return CPIRGLen;
    }

    public void setCpirglen(String CPIRGLen) {
        this.CPIRGLen = CPIRGLen;
    }
    public String getPrtflags() {
        return PrtFlags;
    }

    public void setPrtflags(String PrtFlags) {
        this.PrtFlags = PrtFlags;
    }
    public String getVschar() {
        return VSChar;
    }

    public void setVschar(String VSChar) {
        this.VSChar = VSChar;
    }


}