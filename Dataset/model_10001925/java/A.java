





import java.util.List;
import java.util.ArrayList;

public class A  {

    private String attA;





    private List<B> bs;


    public A(
        String attA    ) {
        this.attA = attA;
        this.bs = new ArrayList<>();
    }

    public A(
        String attA        ArrayList<B> bs    ) {
        this.attA = attA;
        this.bs = bs;
    }

    public String getAtta() {
        return attA;
    }

    public void setAtta(String attA) {
        this.attA = attA;
    }

    public List<B> getBs() {
        return bs;
    }

    public void addB(B b) {
        this.bs.add(b);
    }

}