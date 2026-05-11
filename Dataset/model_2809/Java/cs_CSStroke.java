





import java.util.List;
import java.util.ArrayList;

public class cs_CSStroke  {

    private float width;
    private int join;
    private float dash_phase;
    private float miterlimit;
    private float dash;
    private int cap;





    private cs_CSElement cs_cselement;


    public cs_CSStroke(
        float width,        int join,        float dash_phase,        float miterlimit,        float dash,        int cap    ) {
        this.width = width;
        this.join = join;
        this.dash_phase = dash_phase;
        this.miterlimit = miterlimit;
        this.dash = dash;
        this.cap = cap;
    }


    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public int getJoin() {
        return join;
    }

    public void setJoin(int join) {
        this.join = join;
    }
    public float getDash_phase() {
        return dash_phase;
    }

    public void setDash_phase(float dash_phase) {
        this.dash_phase = dash_phase;
    }
    public float getMiterlimit() {
        return miterlimit;
    }

    public void setMiterlimit(float miterlimit) {
        this.miterlimit = miterlimit;
    }
    public float getDash() {
        return dash;
    }

    public void setDash(float dash) {
        this.dash = dash;
    }
    public int getCap() {
        return cap;
    }

    public void setCap(int cap) {
        this.cap = cap;
    }

    public cs_CSElement getCs_cselement() {
        return cs_cselement;
    }

    public void setCs_cselement(cs_CSElement cs_cselement) {
        this.cs_cselement = cs_cselement;
    }

}