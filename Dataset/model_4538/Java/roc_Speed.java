





import java.util.List;
import java.util.ArrayList;

public class roc_Speed  {

    private String SLOWEST;
    private String SLOW;
    private String FAST;
    private String NORMAL;
    private String FULL;



    public roc_Speed(
        String SLOWEST,        String SLOW,        String FAST,        String NORMAL,        String FULL    ) {
        this.SLOWEST = SLOWEST;
        this.SLOW = SLOW;
        this.FAST = FAST;
        this.NORMAL = NORMAL;
        this.FULL = FULL;
    }


    public String getSlowest() {
        return SLOWEST;
    }

    public void setSlowest(String SLOWEST) {
        this.SLOWEST = SLOWEST;
    }
    public String getSlow() {
        return SLOW;
    }

    public void setSlow(String SLOW) {
        this.SLOW = SLOW;
    }
    public String getFast() {
        return FAST;
    }

    public void setFast(String FAST) {
        this.FAST = FAST;
    }
    public String getNormal() {
        return NORMAL;
    }

    public void setNormal(String NORMAL) {
        this.NORMAL = NORMAL;
    }
    public String getFull() {
        return FULL;
    }

    public void setFull(String FULL) {
        this.FULL = FULL;
    }


}