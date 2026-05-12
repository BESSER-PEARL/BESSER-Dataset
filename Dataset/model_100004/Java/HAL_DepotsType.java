





import java.util.List;
import java.util.ArrayList;

public class HAL_DepotsType extends AbstractDepotType {






    private List<AbstractDepot> abstractdepots;


    public HAL_DepotsType(
    ) {
        super(
        );
        this.abstractdepots = new ArrayList<>();
    }

    public HAL_DepotsType(
        ArrayList<AbstractDepot> abstractdepots    ) {
        this.abstractdepots = abstractdepots;
    }


    public List<AbstractDepot> getAbstractdepots() {
        return abstractdepots;
    }

    public void addAbstractdepot(Abstractdepot abstractdepot) {
        this.abstractdepots.add(abstractdepot);
    }

}