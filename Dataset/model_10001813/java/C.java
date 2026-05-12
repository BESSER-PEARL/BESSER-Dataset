





import java.util.List;
import java.util.ArrayList;

public class C  {

    private int attrC1;
    private String attrC2;





    private List<B> bs;


    public C(
        int attrC1,        String attrC2    ) {
        this.attrC1 = attrC1;
        this.attrC2 = attrC2;
        this.bs = new ArrayList<>();
    }

    public C(
        int attrC1,        String attrC2        ArrayList<B> bs    ) {
        this.attrC1 = attrC1;
        this.attrC2 = attrC2;
        this.bs = bs;
    }

    public int getAttrc1() {
        return attrC1;
    }

    public void setAttrc1(int attrC1) {
        this.attrC1 = attrC1;
    }
    public String getAttrc2() {
        return attrC2;
    }

    public void setAttrc2(String attrC2) {
        this.attrC2 = attrC2;
    }

    public List<B> getBs() {
        return bs;
    }

    public void addB(B b) {
        this.bs.add(b);
    }

}