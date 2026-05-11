





import java.util.List;
import java.util.ArrayList;

public class g_B  {

    private boolean y;





    private List<g_A> g_as;




    private g_B g_b;


    public g_B(
        boolean y    ) {
        this.y = y;
        this.g_as = new ArrayList<>();
    }

    public g_B(
        boolean y        ArrayList<g_A> g_as    ) {
        this.y = y;
        this.g_as = g_as;
    }

    public boolean getY() {
        return y;
    }

    public void setY(boolean y) {
        this.y = y;
    }

    public List<g_A> getG_as() {
        return g_as;
    }

    public void addG_a(G_a g_a) {
        this.g_as.add(g_a);
    }
    public g_B getG_b() {
        return g_b;
    }

    public void setG_b(g_B g_b) {
        this.g_b = g_b;
    }

}