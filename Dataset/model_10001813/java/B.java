





import java.util.List;
import java.util.ArrayList;

public class B  {

    private int attrB1;
    private String attrB2;





    private A a;


    public B(
        int attrB1,        String attrB2    ) {
        this.attrB1 = attrB1;
        this.attrB2 = attrB2;
    }


    public int getAttrb1() {
        return attrB1;
    }

    public void setAttrb1(int attrB1) {
        this.attrB1 = attrB1;
    }
    public String getAttrb2() {
        return attrB2;
    }

    public void setAttrb2(String attrB2) {
        this.attrB2 = attrB2;
    }

    public A getA() {
        return a;
    }

    public void setA(A a) {
        this.a = a;
    }

}