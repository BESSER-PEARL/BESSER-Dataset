




import java.util.UUID;

import java.util.List;
import java.util.ArrayList;

public class statemachine_Statechart  {

    private String name;
    private String UUID;





    private List<statemachine_Transition> statemachine_transitions;




    private List<statemachine_DataElement> statemachine_dataelements;




    private List<statemachine_Region> statemachine_regions;


    public statemachine_Statechart(
        String name,        String UUID    ) {
        this.name = name;
        this.UUID = UUID;
        this.statemachine_transitions = new ArrayList<>();
        this.statemachine_dataelements = new ArrayList<>();
        this.statemachine_regions = new ArrayList<>();
    }

    public statemachine_Statechart(
        String name,        String UUID        ArrayList<statemachine_Transition> statemachine_transitions,        ArrayList<statemachine_DataElement> statemachine_dataelements,        ArrayList<statemachine_Region> statemachine_regions    ) {
        this.name = name;
        this.UUID = UUID;
        this.statemachine_transitions = statemachine_transitions;
        this.statemachine_dataelements = statemachine_dataelements;
        this.statemachine_regions = statemachine_regions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUuid() {
        return UUID;
    }

    public void setUuid(String UUID) {
        this.UUID = UUID;
    }

    public List<statemachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }
    public List<statemachine_DataElement> getStatemachine_dataelements() {
        return statemachine_dataelements;
    }

    public void addStatemachine_dataelement(Statemachine_dataelement statemachine_dataelement) {
        this.statemachine_dataelements.add(statemachine_dataelement);
    }
    public List<statemachine_Region> getStatemachine_regions() {
        return statemachine_regions;
    }

    public void addStatemachine_region(Statemachine_region statemachine_region) {
        this.statemachine_regions.add(statemachine_region);
    }

}