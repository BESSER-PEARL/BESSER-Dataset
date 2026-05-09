





import java.util.List;
import java.util.ArrayList;

public class gastm_TypesCatchBlock extends CatchBlock {






    private List<gastm_Type> gastm_types;


    public gastm_TypesCatchBlock(
    ) {
        super(
        );
        this.gastm_types = new ArrayList<>();
    }

    public gastm_TypesCatchBlock(
        ArrayList<gastm_Type> gastm_types    ) {
        this.gastm_types = gastm_types;
    }


    public List<gastm_Type> getGastm_types() {
        return gastm_types;
    }

    public void addGastm_type(Gastm_type gastm_type) {
        this.gastm_types.add(gastm_type);
    }

}