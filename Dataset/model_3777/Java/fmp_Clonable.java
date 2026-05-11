





import java.util.List;
import java.util.ArrayList;

public class fmp_Clonable extends Node {

    private String state;





    private fmp_Clonable fmp_clonable;




    private List<fmp_Clonable> fmp_clonables;


    public fmp_Clonable(
        String state    ) {
        super(
        );
        this.state = state;
        this.fmp_clonables = new ArrayList<>();
    }

    public fmp_Clonable(
        String state        ArrayList<fmp_Clonable> fmp_clonables    ) {
        this.state = state;
        this.fmp_clonables = fmp_clonables;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public fmp_Clonable getFmp_clonable() {
        return fmp_clonable;
    }

    public void setFmp_clonable(fmp_Clonable fmp_clonable) {
        this.fmp_clonable = fmp_clonable;
    }
    public List<fmp_Clonable> getFmp_clonables() {
        return fmp_clonables;
    }

    public void addFmp_clonable(Fmp_clonable fmp_clonable) {
        this.fmp_clonables.add(fmp_clonable);
    }

}