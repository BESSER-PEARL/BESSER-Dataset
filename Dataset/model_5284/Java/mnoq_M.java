





import java.util.List;
import java.util.ArrayList;

public class mnoq_M  {

    private int x;





    private mnoq_N mnoq_n;




    private mnoq_O mnoq_o;




    private List<mnoq_N> mnoq_ns;


    public mnoq_M(
        int x    ) {
        this.x = x;
        this.mnoq_ns = new ArrayList<>();
    }

    public mnoq_M(
        int x        ArrayList<mnoq_N> mnoq_ns    ) {
        this.x = x;
        this.mnoq_ns = mnoq_ns;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public mnoq_N getMnoq_n() {
        return mnoq_n;
    }

    public void setMnoq_n(mnoq_N mnoq_n) {
        this.mnoq_n = mnoq_n;
    }
    public mnoq_O getMnoq_o() {
        return mnoq_o;
    }

    public void setMnoq_o(mnoq_O mnoq_o) {
        this.mnoq_o = mnoq_o;
    }
    public List<mnoq_N> getMnoq_ns() {
        return mnoq_ns;
    }

    public void addMnoq_n(Mnoq_n mnoq_n) {
        this.mnoq_ns.add(mnoq_n);
    }

}