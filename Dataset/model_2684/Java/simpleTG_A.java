





import java.util.List;
import java.util.ArrayList;

public class simpleTG_A  {






    private List<simpleTG_B> simpletg_bs;




    private simpleTG_Container simpletg_container;


    public simpleTG_A(
    ) {
        this.simpletg_bs = new ArrayList<>();
    }

    public simpleTG_A(
        ArrayList<simpleTG_B> simpletg_bs    ) {
        this.simpletg_bs = simpletg_bs;
    }


    public List<simpleTG_B> getSimpletg_bs() {
        return simpletg_bs;
    }

    public void addSimpletg_b(Simpletg_b simpletg_b) {
        this.simpletg_bs.add(simpletg_b);
    }
    public simpleTG_Container getSimpletg_container() {
        return simpletg_container;
    }

    public void setSimpletg_container(simpleTG_Container simpletg_container) {
        this.simpletg_container = simpletg_container;
    }

}