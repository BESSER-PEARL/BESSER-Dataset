





import java.util.List;
import java.util.ArrayList;

public class pivot_TupleLiteralExp extends LiteralExp {






    private List<pivot_TupleLiteralPart> pivot_tupleliteralparts;


    public pivot_TupleLiteralExp(
    ) {
        super(
        );
        this.pivot_tupleliteralparts = new ArrayList<>();
    }

    public pivot_TupleLiteralExp(
        ArrayList<pivot_TupleLiteralPart> pivot_tupleliteralparts    ) {
        this.pivot_tupleliteralparts = pivot_tupleliteralparts;
    }


    public List<pivot_TupleLiteralPart> getPivot_tupleliteralparts() {
        return pivot_tupleliteralparts;
    }

    public void addPivot_tupleliteralpart(Pivot_tupleliteralpart pivot_tupleliteralpart) {
        this.pivot_tupleliteralparts.add(pivot_tupleliteralpart);
    }

}