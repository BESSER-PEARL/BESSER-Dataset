





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaExecHost extends GaExecHost {

    private String ISRprioRange;
    private String isSched;
    private String schSlack;
    private String schedUtiliz;
    private String ISRswitchT;



    public MARTE_SAM_SaExecHost(
        String ISRprioRange,        String isSched,        String schSlack,        String schedUtiliz,        String ISRswitchT    ) {
        super(
        );
        this.ISRprioRange = ISRprioRange;
        this.isSched = isSched;
        this.schSlack = schSlack;
        this.schedUtiliz = schedUtiliz;
        this.ISRswitchT = ISRswitchT;
    }


    public String getIsrpriorange() {
        return ISRprioRange;
    }

    public void setIsrpriorange(String ISRprioRange) {
        this.ISRprioRange = ISRprioRange;
    }
    public String getIssched() {
        return isSched;
    }

    public void setIssched(String isSched) {
        this.isSched = isSched;
    }
    public String getSchslack() {
        return schSlack;
    }

    public void setSchslack(String schSlack) {
        this.schSlack = schSlack;
    }
    public String getSchedutiliz() {
        return schedUtiliz;
    }

    public void setSchedutiliz(String schedUtiliz) {
        this.schedUtiliz = schedUtiliz;
    }
    public String getIsrswitcht() {
        return ISRswitchT;
    }

    public void setIsrswitcht(String ISRswitchT) {
        this.ISRswitchT = ISRswitchT;
    }


}