





import java.util.List;
import java.util.ArrayList;

public class fxg_Matrix extends FXGElement {

    private String ty;
    private String tx;
    private String c;
    private String d;
    private String b;
    private String a;





    private fxg_Transform fxg_transform;


    public fxg_Matrix(
        String ty,        String tx,        String c,        String d,        String b,        String a    ) {
        super(
        );
        this.ty = ty;
        this.tx = tx;
        this.c = c;
        this.d = d;
        this.b = b;
        this.a = a;
    }


    public String getTy() {
        return ty;
    }

    public void setTy(String ty) {
        this.ty = ty;
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

    public fxg_Transform getFxg_transform() {
        return fxg_transform;
    }

    public void setFxg_transform(fxg_Transform fxg_transform) {
        this.fxg_transform = fxg_transform;
    }

}