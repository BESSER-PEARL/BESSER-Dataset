





import java.util.List;
import java.util.ArrayList;

public class dsl_Model  {






    private List<dsl_Mover> dsl_movers;


    public dsl_Model(
    ) {
        this.dsl_movers = new ArrayList<>();
    }

    public dsl_Model(
        ArrayList<dsl_Mover> dsl_movers    ) {
        this.dsl_movers = dsl_movers;
    }


    public List<dsl_Mover> getDsl_movers() {
        return dsl_movers;
    }

    public void addDsl_mover(Dsl_mover dsl_mover) {
        this.dsl_movers.add(dsl_mover);
    }

}