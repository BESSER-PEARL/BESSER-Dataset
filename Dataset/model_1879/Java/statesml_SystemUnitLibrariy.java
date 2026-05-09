





import java.util.List;
import java.util.ArrayList;

public class statesml_SystemUnitLibrariy  {

    private String name;





    private List<statesml_SystemUnits> statesml_systemunitss;


    public statesml_SystemUnitLibrariy(
        String name    ) {
        this.name = name;
        this.statesml_systemunitss = new ArrayList<>();
    }

    public statesml_SystemUnitLibrariy(
        String name        ArrayList<statesml_SystemUnits> statesml_systemunitss    ) {
        this.name = name;
        this.statesml_systemunitss = statesml_systemunitss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<statesml_SystemUnits> getStatesml_systemunitss() {
        return statesml_systemunitss;
    }

    public void addStatesml_systemunits(Statesml_systemunits statesml_systemunits) {
        this.statesml_systemunitss.add(statesml_systemunits);
    }

}