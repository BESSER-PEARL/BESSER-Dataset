





import java.util.List;
import java.util.ArrayList;

public class gast_accesses_FunctionAccess extends Access {






    private List<GASTType> gasttypes;


    public gast_accesses_FunctionAccess(
    ) {
        super(
        );
        this.gasttypes = new ArrayList<>();
    }

    public gast_accesses_FunctionAccess(
        ArrayList<GASTType> gasttypes    ) {
        this.gasttypes = gasttypes;
    }


    public List<GASTType> getGasttypes() {
        return gasttypes;
    }

    public void addGasttype(Gasttype gasttype) {
        this.gasttypes.add(gasttype);
    }

}