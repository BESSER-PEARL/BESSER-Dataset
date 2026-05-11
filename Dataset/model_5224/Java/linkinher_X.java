





import java.util.List;
import java.util.ArrayList;

public class linkinher_X  {






    private linkinher_N linkinher_n;




    private List<linkinher_Named> linkinher_nameds;


    public linkinher_X(
    ) {
        this.linkinher_nameds = new ArrayList<>();
    }

    public linkinher_X(
        ArrayList<linkinher_Named> linkinher_nameds    ) {
        this.linkinher_nameds = linkinher_nameds;
    }


    public linkinher_N getLinkinher_n() {
        return linkinher_n;
    }

    public void setLinkinher_n(linkinher_N linkinher_n) {
        this.linkinher_n = linkinher_n;
    }
    public List<linkinher_Named> getLinkinher_nameds() {
        return linkinher_nameds;
    }

    public void addLinkinher_named(Linkinher_named linkinher_named) {
        this.linkinher_nameds.add(linkinher_named);
    }

}