





import java.util.List;
import java.util.ArrayList;

public class link_C extends Named {






    private link_A link_a;




    private List<link_D> link_ds;




    private link_B link_b;




    private link_W link_w;


    public link_C(
    ) {
        super(
        );
        this.link_ds = new ArrayList<>();
    }

    public link_C(
        ArrayList<link_D> link_ds    ) {
        this.link_ds = link_ds;
    }


    public link_A getLink_a() {
        return link_a;
    }

    public void setLink_a(link_A link_a) {
        this.link_a = link_a;
    }
    public List<link_D> getLink_ds() {
        return link_ds;
    }

    public void addLink_d(Link_d link_d) {
        this.link_ds.add(link_d);
    }
    public link_B getLink_b() {
        return link_b;
    }

    public void setLink_b(link_B link_b) {
        this.link_b = link_b;
    }
    public link_W getLink_w() {
        return link_w;
    }

    public void setLink_w(link_W link_w) {
        this.link_w = link_w;
    }

}