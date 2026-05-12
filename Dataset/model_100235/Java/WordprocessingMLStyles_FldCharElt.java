





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLStyles_FldCharElt  {

    private None fldLock;
    private None fldCharType;





    private StringType stringtype;


    public WordprocessingMLStyles_FldCharElt(
        None fldLock,        None fldCharType    ) {
        this.fldLock = fldLock;
        this.fldCharType = fldCharType;
    }


    public None getFldlock() {
        return fldLock;
    }

    public void setFldlock(None fldLock) {
        this.fldLock = fldLock;
    }
    public None getFldchartype() {
        return fldCharType;
    }

    public void setFldchartype(None fldCharType) {
        this.fldCharType = fldCharType;
    }

    public StringType getStringtype() {
        return stringtype;
    }

    public void setStringtype(StringType stringtype) {
        this.stringtype = stringtype;
    }

}