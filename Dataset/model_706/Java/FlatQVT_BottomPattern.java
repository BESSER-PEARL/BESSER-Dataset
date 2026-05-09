





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_BottomPattern extends CorePattern {






    private List<RealizedVariable> realizedvariables;


    public FlatQVT_BottomPattern(
    ) {
        super(
        );
        this.realizedvariables = new ArrayList<>();
    }

    public FlatQVT_BottomPattern(
        ArrayList<RealizedVariable> realizedvariables    ) {
        this.realizedvariables = realizedvariables;
    }


    public List<RealizedVariable> getRealizedvariables() {
        return realizedvariables;
    }

    public void addRealizedvariable(Realizedvariable realizedvariable) {
        this.realizedvariables.add(realizedvariable);
    }

}