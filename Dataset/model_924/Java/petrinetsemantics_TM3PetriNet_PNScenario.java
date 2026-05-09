





import java.util.List;
import java.util.ArrayList;

public class petrinetsemantics_TM3PetriNet_PNScenario  {






    private List<PNSimEvent> pnsimevents;


    public petrinetsemantics_TM3PetriNet_PNScenario(
    ) {
        this.pnsimevents = new ArrayList<>();
    }

    public petrinetsemantics_TM3PetriNet_PNScenario(
        ArrayList<PNSimEvent> pnsimevents    ) {
        this.pnsimevents = pnsimevents;
    }


    public List<PNSimEvent> getPnsimevents() {
        return pnsimevents;
    }

    public void addPnsimevent(Pnsimevent pnsimevent) {
        this.pnsimevents.add(pnsimevent);
    }

}