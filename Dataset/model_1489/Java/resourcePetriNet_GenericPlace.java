





import java.util.List;
import java.util.ArrayList;

public class resourcePetriNet_GenericPlace  {

    private String name;
    private int numberOfTokens;





    private resourcePetriNet_OutputArc resourcepetrinet_outputarc;




    private resourcePetriNet_InputArc resourcepetrinet_inputarc;




    private resourcePetriNet_PetriNet resourcepetrinet_petrinet;


    public resourcePetriNet_GenericPlace(
        String name,        int numberOfTokens    ) {
        this.name = name;
        this.numberOfTokens = numberOfTokens;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNumberoftokens() {
        return numberOfTokens;
    }

    public void setNumberoftokens(int numberOfTokens) {
        this.numberOfTokens = numberOfTokens;
    }

    public resourcePetriNet_OutputArc getResourcepetrinet_outputarc() {
        return resourcepetrinet_outputarc;
    }

    public void setResourcepetrinet_outputarc(resourcePetriNet_OutputArc resourcepetrinet_outputarc) {
        this.resourcepetrinet_outputarc = resourcepetrinet_outputarc;
    }
    public resourcePetriNet_InputArc getResourcepetrinet_inputarc() {
        return resourcepetrinet_inputarc;
    }

    public void setResourcepetrinet_inputarc(resourcePetriNet_InputArc resourcepetrinet_inputarc) {
        this.resourcepetrinet_inputarc = resourcepetrinet_inputarc;
    }
    public resourcePetriNet_PetriNet getResourcepetrinet_petrinet() {
        return resourcepetrinet_petrinet;
    }

    public void setResourcepetrinet_petrinet(resourcePetriNet_PetriNet resourcepetrinet_petrinet) {
        this.resourcepetrinet_petrinet = resourcepetrinet_petrinet;
    }

}