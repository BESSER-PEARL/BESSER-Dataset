





import java.util.List;
import java.util.ArrayList;

public class A1  {

    private String attA;





    private List<B1> b1s;


    public A1(
        String attA    ) {
        this.attA = attA;
        this.b1s = new ArrayList<>();
    }

    public A1(
        String attA        ArrayList<B1> b1s    ) {
        this.attA = attA;
        this.b1s = b1s;
    }

    public String getAtta() {
        return attA;
    }

    public void setAtta(String attA) {
        this.attA = attA;
    }

    public List<B1> getB1s() {
        return b1s;
    }

    public void addB1(B1 b1) {
        this.b1s.add(b1);
    }

}