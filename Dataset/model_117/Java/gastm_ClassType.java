





import java.util.List;
import java.util.ArrayList;

public class gastm_ClassType extends AggregateType {






    private List<gastm_DerivesFrom> gastm_derivesfroms;


    public gastm_ClassType(
    ) {
        super(
        );
        this.gastm_derivesfroms = new ArrayList<>();
    }

    public gastm_ClassType(
        ArrayList<gastm_DerivesFrom> gastm_derivesfroms    ) {
        this.gastm_derivesfroms = gastm_derivesfroms;
    }


    public List<gastm_DerivesFrom> getGastm_derivesfroms() {
        return gastm_derivesfroms;
    }

    public void addGastm_derivesfrom(Gastm_derivesfrom gastm_derivesfrom) {
        this.gastm_derivesfroms.add(gastm_derivesfrom);
    }

}