





import java.util.List;
import java.util.ArrayList;

public class dg_Matrix extends Transform {

    private String e;
    private String c;
    private String f;
    private String d;
    private String b;
    private String a;



    public dg_Matrix(
        String e,        String c,        String f,        String d,        String b,        String a    ) {
        super(
        );
        this.e = e;
        this.c = c;
        this.f = f;
        this.d = d;
        this.b = b;
        this.a = a;
    }


    public String getE() {
        return e;
    }

    public void setE(String e) {
        this.e = e;
    }
    public String getC() {
        return c;
    }

    public void setC(String c) {
        this.c = c;
    }
    public String getF() {
        return f;
    }

    public void setF(String f) {
        this.f = f;
    }
    public String getD() {
        return d;
    }

    public void setD(String d) {
        this.d = d;
    }
    public String getB() {
        return b;
    }

    public void setB(String b) {
        this.b = b;
    }
    public String getA() {
        return a;
    }

    public void setA(String a) {
        this.a = a;
    }


}