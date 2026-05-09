





import java.util.List;
import java.util.ArrayList;

public class astm_ClassType extends AggregateType {






    private List<astm_DerivesFrom> astm_derivesfroms;


    public astm_ClassType(
    ) {
        super(
        );
        this.astm_derivesfroms = new ArrayList<>();
    }

    public astm_ClassType(
        ArrayList<astm_DerivesFrom> astm_derivesfroms    ) {
        this.astm_derivesfroms = astm_derivesfroms;
    }


    public List<astm_DerivesFrom> getAstm_derivesfroms() {
        return astm_derivesfroms;
    }

    public void addAstm_derivesfrom(Astm_derivesfrom astm_derivesfrom) {
        this.astm_derivesfroms.add(astm_derivesfrom);
    }

}