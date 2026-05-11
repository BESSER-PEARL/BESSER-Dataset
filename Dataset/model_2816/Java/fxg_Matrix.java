





import java.util.List;
import java.util.ArrayList;

public class fxg_Matrix extends FXGElement {

    private String b;
    private String ty;
    private String d;
    private String a;
    private String tx;
    private String c;



    public fxg_Matrix(
        String b,        String ty,        String d,        String a,        String tx,        String c    ) {
        super(
        );
        this.b = b;
        this.ty = ty;
        this.d = d;
        this.a = a;
        this.tx = tx;
        this.c = c;
    }


    public String getB() {
        return b;
    }

    public void setB(String b) {
        this.b = b;
    }
    public String getTy() {
        return ty;
    }

    public void setTy(String ty) {
        this.ty = ty;
    }
    public String getD() {
        return d;
    }

    public void setD(String d) {
        this.d = d;
    }
    public String getA() {
        return a;
    }

    public void setA(String a) {
        this.a = a;
    }
    public String getTx() {
        return tx;
    }

    public void setTx(String tx) {
        this.tx = tx;
    }
    public String getC() {
        return c;
    }

    public void setC(String c) {
        this.c = c;
    }


}