





import java.util.List;
import java.util.ArrayList;

public class statesml_SystemUnitLibrary  {

    private String name;





    private List<statesml_SystemUnit> statesml_systemunits;


    public statesml_SystemUnitLibrary(
        String name    ) {
        this.name = name;
        this.statesml_systemunits = new ArrayList<>();
    }

    public statesml_SystemUnitLibrary(
        String name        ArrayList<statesml_SystemUnit> statesml_systemunits    ) {
        this.name = name;
        this.statesml_systemunits = statesml_systemunits;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<statesml_SystemUnit> getStatesml_systemunits() {
        return statesml_systemunits;
    }

    public void addStatesml_systemunit(Statesml_systemunit statesml_systemunit) {
        this.statesml_systemunits.add(statesml_systemunit);
    }

}