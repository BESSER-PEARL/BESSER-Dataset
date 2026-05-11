





import java.util.List;
import java.util.ArrayList;

public class sbase_SRoot extends SElement {






    private List<sbase_X> sbase_xs;


    public sbase_SRoot(
    ) {
        super(
        );
        this.sbase_xs = new ArrayList<>();
    }

    public sbase_SRoot(
        ArrayList<sbase_X> sbase_xs    ) {
        this.sbase_xs = sbase_xs;
    }


    public List<sbase_X> getSbase_xs() {
        return sbase_xs;
    }

    public void addSbase_x(Sbase_x sbase_x) {
        this.sbase_xs.add(sbase_x);
    }

}