





import java.util.List;
import java.util.ArrayList;

public class express_core_ParameterType  {






    private List<GeneralizedType> generalizedtypes;


    public express_core_ParameterType(
    ) {
        this.generalizedtypes = new ArrayList<>();
    }

    public express_core_ParameterType(
        ArrayList<GeneralizedType> generalizedtypes    ) {
        this.generalizedtypes = generalizedtypes;
    }


    public List<GeneralizedType> getGeneralizedtypes() {
        return generalizedtypes;
    }

    public void addGeneralizedtype(Generalizedtype generalizedtype) {
        this.generalizedtypes.add(generalizedtype);
    }

}