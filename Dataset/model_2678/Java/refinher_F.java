





import java.util.List;
import java.util.ArrayList;

public class refinher_F  {






    private List<refinher_G> refinher_gs;




    private List<refinher_H> refinher_hs;


    public refinher_F(
    ) {
        this.refinher_gs = new ArrayList<>();
        this.refinher_hs = new ArrayList<>();
    }

    public refinher_F(
        ArrayList<refinher_G> refinher_gs,        ArrayList<refinher_H> refinher_hs    ) {
        this.refinher_gs = refinher_gs;
        this.refinher_hs = refinher_hs;
    }


    public List<refinher_G> getRefinher_gs() {
        return refinher_gs;
    }

    public void addRefinher_g(Refinher_g refinher_g) {
        this.refinher_gs.add(refinher_g);
    }
    public List<refinher_H> getRefinher_hs() {
        return refinher_hs;
    }

    public void addRefinher_h(Refinher_h refinher_h) {
        this.refinher_hs.add(refinher_h);
    }

}