





import java.util.List;
import java.util.ArrayList;

public class C2  {

    private String attribute;
    private int C2ID;
    private int C1ID;





    private C1 c1;


    public C2(
        String attribute,        int C2ID,        int C1ID    ) {
        this.attribute = attribute;
        this.C2ID = C2ID;
        this.C1ID = C1ID;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getC2id() {
        return C2ID;
    }

    public void setC2id(int C2ID) {
        this.C2ID = C2ID;
    }
    public int getC1id() {
        return C1ID;
    }

    public void setC1id(int C1ID) {
        this.C1ID = C1ID;
    }

    public C1 getC1() {
        return c1;
    }

    public void setC1(C1 c1) {
        this.c1 = c1;
    }

}