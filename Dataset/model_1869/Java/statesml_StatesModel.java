





import java.util.List;
import java.util.ArrayList;

public class statesml_StatesModel  {






    private List<statesml_SystemUnitModel> statesml_systemunitmodels;


    public statesml_StatesModel(
    ) {
        this.statesml_systemunitmodels = new ArrayList<>();
    }

    public statesml_StatesModel(
        ArrayList<statesml_SystemUnitModel> statesml_systemunitmodels    ) {
        this.statesml_systemunitmodels = statesml_systemunitmodels;
    }


    public List<statesml_SystemUnitModel> getStatesml_systemunitmodels() {
        return statesml_systemunitmodels;
    }

    public void addStatesml_systemunitmodel(Statesml_systemunitmodel statesml_systemunitmodel) {
        this.statesml_systemunitmodels.add(statesml_systemunitmodel);
    }

}