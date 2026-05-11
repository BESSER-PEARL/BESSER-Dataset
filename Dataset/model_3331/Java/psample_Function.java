





import java.util.List;
import java.util.ArrayList;

public class psample_Function extends Member {






    private List<psample_PrimitiveTypeVariable> psample_primitivetypevariables;


    public psample_Function(
    ) {
        super(
        );
        this.psample_primitivetypevariables = new ArrayList<>();
    }

    public psample_Function(
        ArrayList<psample_PrimitiveTypeVariable> psample_primitivetypevariables    ) {
        this.psample_primitivetypevariables = psample_primitivetypevariables;
    }


    public List<psample_PrimitiveTypeVariable> getPsample_primitivetypevariables() {
        return psample_primitivetypevariables;
    }

    public void addPsample_primitivetypevariable(Psample_primitivetypevariable psample_primitivetypevariable) {
        this.psample_primitivetypevariables.add(psample_primitivetypevariable);
    }

}