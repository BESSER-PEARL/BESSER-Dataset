





import java.util.List;
import java.util.ArrayList;

public class C  {

    private boolean attC2;
    private int attC1;





    private List<B> bs;


    public C(
        boolean attC2,        int attC1    ) {
        this.attC2 = attC2;
        this.attC1 = attC1;
        this.bs = new ArrayList<>();
    }

    public C(
        boolean attC2,        int attC1        ArrayList<B> bs    ) {
        this.attC2 = attC2;
        this.attC1 = attC1;
        this.bs = bs;
    }

    public boolean getAttc2() {
        return attC2;
    }

    public void setAttc2(boolean attC2) {
        this.attC2 = attC2;
    }
    public int getAttc1() {
        return attC1;
    }

    public void setAttc1(int attC1) {
        this.attC1 = attC1;
    }

    public List<B> getBs() {
        return bs;
    }

    public void addB(B b) {
        this.bs.add(b);
    }

}