





import java.util.List;
import java.util.ArrayList;

public class afpText_CPIRG  {

    private String GCGID;
    private String Count;
    private String PrtFlags;
    private String CodePoint;





    private afpText_CPI afptext_cpi;


    public afpText_CPIRG(
        String GCGID,        String Count,        String PrtFlags,        String CodePoint    ) {
        this.GCGID = GCGID;
        this.Count = Count;
        this.PrtFlags = PrtFlags;
        this.CodePoint = CodePoint;
    }


    public String getGcgid() {
        return GCGID;
    }

    public void setGcgid(String GCGID) {
        this.GCGID = GCGID;
    }
    public String getCount() {
        return Count;
    }

    public void setCount(String Count) {
        this.Count = Count;
    }
    public String getPrtflags() {
        return PrtFlags;
    }

    public void setPrtflags(String PrtFlags) {
        this.PrtFlags = PrtFlags;
    }
    public String getCodepoint() {
        return CodePoint;
    }

    public void setCodepoint(String CodePoint) {
        this.CodePoint = CodePoint;
    }

    public afpText_CPI getAfptext_cpi() {
        return afptext_cpi;
    }

    public void setAfptext_cpi(afpText_CPI afptext_cpi) {
        this.afptext_cpi = afptext_cpi;
    }

}