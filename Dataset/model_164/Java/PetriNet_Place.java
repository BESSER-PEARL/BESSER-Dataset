





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Place extends Identifiable {

    private String name;





    private List<PetriNet_Token> petrinet_tokens;




    private PetriNet_InputArc petrinet_inputarc;




    private List<PetriNet_InputArc> petrinet_inputarcs;




    private PetriNet_OutputArc petrinet_outputarc;




    private List<PetriNet_OutputArc> petrinet_outputarcs;


    public PetriNet_Place(
        String name    ) {
        super(
        );
        this.name = name;
        this.petrinet_tokens = new ArrayList<>();
        this.petrinet_inputarcs = new ArrayList<>();
        this.petrinet_outputarcs = new ArrayList<>();
    }

    public PetriNet_Place(
        String name        ArrayList<PetriNet_Token> petrinet_tokens,        ArrayList<PetriNet_InputArc> petrinet_inputarcs,        ArrayList<PetriNet_OutputArc> petrinet_outputarcs    ) {
        this.name = name;
        this.petrinet_tokens = petrinet_tokens;
        this.petrinet_inputarcs = petrinet_inputarcs;
        this.petrinet_outputarcs = petrinet_outputarcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PetriNet_Token> getPetrinet_tokens() {
        return petrinet_tokens;
    }

    public void addPetrinet_token(Petrinet_token petrinet_token) {
        this.petrinet_tokens.add(petrinet_token);
    }
    public PetriNet_InputArc getPetrinet_inputarc() {
        return petrinet_inputarc;
    }

    public void setPetrinet_inputarc(PetriNet_InputArc petrinet_inputarc) {
        this.petrinet_inputarc = petrinet_inputarc;
    }
    public List<PetriNet_InputArc> getPetrinet_inputarcs() {
        return petrinet_inputarcs;
    }

    public void addPetrinet_inputarc(Petrinet_inputarc petrinet_inputarc) {
        this.petrinet_inputarcs.add(petrinet_inputarc);
    }
    public PetriNet_OutputArc getPetrinet_outputarc() {
        return petrinet_outputarc;
    }

    public void setPetrinet_outputarc(PetriNet_OutputArc petrinet_outputarc) {
        this.petrinet_outputarc = petrinet_outputarc;
    }
    public List<PetriNet_OutputArc> getPetrinet_outputarcs() {
        return petrinet_outputarcs;
    }

    public void addPetrinet_outputarc(Petrinet_outputarc petrinet_outputarc) {
        this.petrinet_outputarcs.add(petrinet_outputarc);
    }

}