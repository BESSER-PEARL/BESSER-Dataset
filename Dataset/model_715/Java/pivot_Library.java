





import java.util.List;
import java.util.ArrayList;

public class pivot_Library extends Package {






    private List<pivot_Precedence> pivot_precedences;


    public pivot_Library(
    ) {
        super(
        );
        this.pivot_precedences = new ArrayList<>();
    }

    public pivot_Library(
        ArrayList<pivot_Precedence> pivot_precedences    ) {
        this.pivot_precedences = pivot_precedences;
    }


    public List<pivot_Precedence> getPivot_precedences() {
        return pivot_precedences;
    }

    public void addPivot_precedence(Pivot_precedence pivot_precedence) {
        this.pivot_precedences.add(pivot_precedence);
    }

}