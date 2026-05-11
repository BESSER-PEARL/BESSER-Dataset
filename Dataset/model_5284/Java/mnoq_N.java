





import java.util.List;
import java.util.ArrayList;

public class mnoq_N  {

    private int x;





    private mnoq_Foo mnoq_foo;




    private mnoq_Q mnoq_q;




    private List<mnoq_Q> mnoq_qs;


    public mnoq_N(
        int x    ) {
        this.x = x;
        this.mnoq_qs = new ArrayList<>();
    }

    public mnoq_N(
        int x        ArrayList<mnoq_Q> mnoq_qs    ) {
        this.x = x;
        this.mnoq_qs = mnoq_qs;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public mnoq_Foo getMnoq_foo() {
        return mnoq_foo;
    }

    public void setMnoq_foo(mnoq_Foo mnoq_foo) {
        this.mnoq_foo = mnoq_foo;
    }
    public mnoq_Q getMnoq_q() {
        return mnoq_q;
    }

    public void setMnoq_q(mnoq_Q mnoq_q) {
        this.mnoq_q = mnoq_q;
    }
    public List<mnoq_Q> getMnoq_qs() {
        return mnoq_qs;
    }

    public void addMnoq_q(Mnoq_q mnoq_q) {
        this.mnoq_qs.add(mnoq_q);
    }

}