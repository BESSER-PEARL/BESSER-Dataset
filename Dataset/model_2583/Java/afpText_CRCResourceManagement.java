





import java.util.List;
import java.util.ArrayList;

public class afpText_CRCResourceManagement extends triplet {

    private String ResClassFlg;
    private String RMValue;
    private String FmtQual;



    public afpText_CRCResourceManagement(
        String ResClassFlg,        String RMValue,        String FmtQual    ) {
        super(
        );
        this.ResClassFlg = ResClassFlg;
        this.RMValue = RMValue;
        this.FmtQual = FmtQual;
    }


    public String getResclassflg() {
        return ResClassFlg;
    }

    public void setResclassflg(String ResClassFlg) {
        this.ResClassFlg = ResClassFlg;
    }
    public String getRmvalue() {
        return RMValue;
    }

    public void setRmvalue(String RMValue) {
        this.RMValue = RMValue;
    }
    public String getFmtqual() {
        return FmtQual;
    }

    public void setFmtqual(String FmtQual) {
        this.FmtQual = FmtQual;
    }


}