





import java.util.List;
import java.util.ArrayList;

public class link_X extends Named {






    private List<link_K> link_ks;




    private List<link_A> link_as;


    public link_X(
    ) {
        super(
        );
        this.link_ks = new ArrayList<>();
        this.link_as = new ArrayList<>();
    }

    public link_X(
        ArrayList<link_K> link_ks,        ArrayList<link_A> link_as    ) {
        this.link_ks = link_ks;
        this.link_as = link_as;
    }


    public List<link_K> getLink_ks() {
        return link_ks;
    }

    public void addLink_k(Link_k link_k) {
        this.link_ks.add(link_k);
    }
    public List<link_A> getLink_as() {
        return link_as;
    }

    public void addLink_a(Link_a link_a) {
        this.link_as.add(link_a);
    }

}