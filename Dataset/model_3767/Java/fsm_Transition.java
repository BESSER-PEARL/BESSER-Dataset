





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition  {

    private String c;
    private String a;
    private String b;



    public fsm_Transition(
        String c,        String a,        String b    ) {
        this.c = c;
        this.a = a;
        this.b = b;
    }


    public String getC() {
        return c;
    }

    public void setC(String c) {
        this.c = c;
    }
    public String getA() {
        return a;
    }

    public void setA(String a) {
        this.a = a;
    }
    public String getB() {
        return b;
    }

    public void setB(String b) {
        this.b = b;
    }


}