





import java.util.List;
import java.util.ArrayList;

public class A  {

    private int attA;





    private List<B> bs;


    public A(
        int attA    ) {
        this.attA = attA;
        this.bs = new ArrayList<>();
    }

    public A(
        int attA        ArrayList<B> bs    ) {
        this.attA = attA;
        this.bs = bs;
    }

    public int getAtta() {
        return attA;
    }

    public void setAtta(int attA) {
        this.attA = attA;
    }

    public List<B> getBs() {
        return bs;
    }

    public void addB(B b) {
        this.bs.add(b);
    }

}