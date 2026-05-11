





import java.util.List;
import java.util.ArrayList;

public class simplecont_X  {






    private List<simplecont_A> simplecont_as;


    public simplecont_X(
    ) {
        this.simplecont_as = new ArrayList<>();
    }

    public simplecont_X(
        ArrayList<simplecont_A> simplecont_as    ) {
        this.simplecont_as = simplecont_as;
    }


    public List<simplecont_A> getSimplecont_as() {
        return simplecont_as;
    }

    public void addSimplecont_a(Simplecont_a simplecont_a) {
        this.simplecont_as.add(simplecont_a);
    }

}