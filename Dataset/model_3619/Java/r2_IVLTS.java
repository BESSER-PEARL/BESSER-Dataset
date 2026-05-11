





import java.util.List;
import java.util.ArrayList;

public class r2_IVLTS extends IVL {

    private String highClosed;
    private String lowClosed;





    private r2_TS r2_ts;




    private r2_TS r2_ts;




    private r2_PIVLTS r2_pivlts;


    public r2_IVLTS(
        String highClosed,        String lowClosed    ) {
        super(
        );
        this.highClosed = highClosed;
        this.lowClosed = lowClosed;
    }


    public String getHighclosed() {
        return highClosed;
    }

    public void setHighclosed(String highClosed) {
        this.highClosed = highClosed;
    }
    public String getLowclosed() {
        return lowClosed;
    }

    public void setLowclosed(String lowClosed) {
        this.lowClosed = lowClosed;
    }

    public r2_TS getR2_ts() {
        return r2_ts;
    }

    public void setR2_ts(r2_TS r2_ts) {
        this.r2_ts = r2_ts;
    }
    public r2_TS getR2_ts() {
        return r2_ts;
    }

    public void setR2_ts(r2_TS r2_ts) {
        this.r2_ts = r2_ts;
    }
    public r2_PIVLTS getR2_pivlts() {
        return r2_pivlts;
    }

    public void setR2_pivlts(r2_PIVLTS r2_pivlts) {
        this.r2_pivlts = r2_pivlts;
    }

}