





import java.util.List;
import java.util.ArrayList;

public class pivot_MapLiteralExp extends LiteralExp {






    private List<pivot_MapLiteralPart> pivot_mapliteralparts;


    public pivot_MapLiteralExp(
    ) {
        super(
        );
        this.pivot_mapliteralparts = new ArrayList<>();
    }

    public pivot_MapLiteralExp(
        ArrayList<pivot_MapLiteralPart> pivot_mapliteralparts    ) {
        this.pivot_mapliteralparts = pivot_mapliteralparts;
    }


    public List<pivot_MapLiteralPart> getPivot_mapliteralparts() {
        return pivot_mapliteralparts;
    }

    public void addPivot_mapliteralpart(Pivot_mapliteralpart pivot_mapliteralpart) {
        this.pivot_mapliteralparts.add(pivot_mapliteralpart);
    }

}