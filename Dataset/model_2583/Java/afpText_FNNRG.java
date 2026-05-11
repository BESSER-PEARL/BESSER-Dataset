





import java.util.List;
import java.util.ArrayList;

public class afpText_FNNRG  {

    private String TSOffset;
    private String GCGID;



    public afpText_FNNRG(
        String TSOffset,        String GCGID    ) {
        this.TSOffset = TSOffset;
        this.GCGID = GCGID;
    }


    public String getTsoffset() {
        return TSOffset;
    }

    public void setTsoffset(String TSOffset) {
        this.TSOffset = TSOffset;
    }
    public String getGcgid() {
        return GCGID;
    }

    public void setGcgid(String GCGID) {
        this.GCGID = GCGID;
    }


}