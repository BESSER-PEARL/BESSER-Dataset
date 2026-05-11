





import java.util.List;
import java.util.ArrayList;

public class dml_TE  {

    private float d;
    private int i;
    private String s;
    private String b;





    private dml_DI dml_di;




    private dml_FC dml_fc;




    private dml_E dml_e;


    public dml_TE(
        float d,        int i,        String s,        String b    ) {
        this.d = d;
        this.i = i;
        this.s = s;
        this.b = b;
    }


    public float getD() {
        return d;
    }

    public void setD(float d) {
        this.d = d;
    }
    public int getI() {
        return i;
    }

    public void setI(int i) {
        this.i = i;
    }
    public String getS() {
        return s;
    }

    public void setS(String s) {
        this.s = s;
    }
    public String getB() {
        return b;
    }

    public void setB(String b) {
        this.b = b;
    }

    public dml_DI getDml_di() {
        return dml_di;
    }

    public void setDml_di(dml_DI dml_di) {
        this.dml_di = dml_di;
    }
    public dml_FC getDml_fc() {
        return dml_fc;
    }

    public void setDml_fc(dml_FC dml_fc) {
        this.dml_fc = dml_fc;
    }
    public dml_E getDml_e() {
        return dml_e;
    }

    public void setDml_e(dml_E dml_e) {
        this.dml_e = dml_e;
    }

}