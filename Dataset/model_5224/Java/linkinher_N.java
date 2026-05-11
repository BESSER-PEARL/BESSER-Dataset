





import java.util.List;
import java.util.ArrayList;

public class linkinher_N extends S, T, Named {






    private linkinher_E linkinher_e;




    private List<linkinher_E> linkinher_es;




    private linkinher_E linkinher_e;


    public linkinher_N(
    ) {
        super(
        );
        this.linkinher_es = new ArrayList<>();
    }

    public linkinher_N(
        ArrayList<linkinher_E> linkinher_es    ) {
        this.linkinher_es = linkinher_es;
    }


    public linkinher_E getLinkinher_e() {
        return linkinher_e;
    }

    public void setLinkinher_e(linkinher_E linkinher_e) {
        this.linkinher_e = linkinher_e;
    }
    public List<linkinher_E> getLinkinher_es() {
        return linkinher_es;
    }

    public void addLinkinher_e(Linkinher_e linkinher_e) {
        this.linkinher_es.add(linkinher_e);
    }
    public linkinher_E getLinkinher_e() {
        return linkinher_e;
    }

    public void setLinkinher_e(linkinher_E linkinher_e) {
        this.linkinher_e = linkinher_e;
    }

}