





import java.util.List;
import java.util.ArrayList;

public class multiview3_C extends Named {






    private List<multiview3_H> multiview3_hs;




    private multiview3_W multiview3_w;




    private multiview3_B multiview3_b;




    private List<multiview3_K> multiview3_ks;


    public multiview3_C(
    ) {
        super(
        );
        this.multiview3_hs = new ArrayList<>();
        this.multiview3_ks = new ArrayList<>();
    }

    public multiview3_C(
        ArrayList<multiview3_H> multiview3_hs,        ArrayList<multiview3_K> multiview3_ks    ) {
        this.multiview3_hs = multiview3_hs;
        this.multiview3_ks = multiview3_ks;
    }


    public List<multiview3_H> getMultiview3_hs() {
        return multiview3_hs;
    }

    public void addMultiview3_h(Multiview3_h multiview3_h) {
        this.multiview3_hs.add(multiview3_h);
    }
    public multiview3_W getMultiview3_w() {
        return multiview3_w;
    }

    public void setMultiview3_w(multiview3_W multiview3_w) {
        this.multiview3_w = multiview3_w;
    }
    public multiview3_B getMultiview3_b() {
        return multiview3_b;
    }

    public void setMultiview3_b(multiview3_B multiview3_b) {
        this.multiview3_b = multiview3_b;
    }
    public List<multiview3_K> getMultiview3_ks() {
        return multiview3_ks;
    }

    public void addMultiview3_k(Multiview3_k multiview3_k) {
        this.multiview3_ks.add(multiview3_k);
    }

}