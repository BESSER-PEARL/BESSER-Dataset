





import java.util.List;
import java.util.ArrayList;

public class simpleTG_Container  {






    private List<simpleTG_B> simpletg_bs;




    private List<simpleTG_C> simpletg_cs;


    public simpleTG_Container(
    ) {
        this.simpletg_bs = new ArrayList<>();
        this.simpletg_cs = new ArrayList<>();
    }

    public simpleTG_Container(
        ArrayList<simpleTG_B> simpletg_bs,        ArrayList<simpleTG_C> simpletg_cs    ) {
        this.simpletg_bs = simpletg_bs;
        this.simpletg_cs = simpletg_cs;
    }


    public List<simpleTG_B> getSimpletg_bs() {
        return simpletg_bs;
    }

    public void addSimpletg_b(Simpletg_b simpletg_b) {
        this.simpletg_bs.add(simpletg_b);
    }
    public List<simpleTG_C> getSimpletg_cs() {
        return simpletg_cs;
    }

    public void addSimpletg_c(Simpletg_c simpletg_c) {
        this.simpletg_cs.add(simpletg_c);
    }

}