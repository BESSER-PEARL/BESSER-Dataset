





import java.util.List;
import java.util.ArrayList;

public class C1  {

    private int attC1;
    private boolean attC2;





    private List<B1> b1s;


    public C1(
        int attC1,        boolean attC2    ) {
        this.attC1 = attC1;
        this.attC2 = attC2;
        this.b1s = new ArrayList<>();
    }

    public C1(
        int attC1,        boolean attC2        ArrayList<B1> b1s    ) {
        this.attC1 = attC1;
        this.attC2 = attC2;
        this.b1s = b1s;
    }

    public int getAttc1() {
        return attC1;
    }

    public void setAttc1(int attC1) {
        this.attC1 = attC1;
    }
    public boolean getAttc2() {
        return attC2;
    }

    public void setAttc2(boolean attC2) {
        this.attC2 = attC2;
    }

    public List<B1> getB1s() {
        return b1s;
    }

    public void addB1(B1 b1) {
        this.b1s.add(b1);
    }

}