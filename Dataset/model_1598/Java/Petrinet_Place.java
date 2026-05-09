





import java.util.List;
import java.util.ArrayList;

public class Petrinet_Place extends Node {






    private Petrinet_OutputArc petrinet_outputarc;




    private Petrinet_InputArc petrinet_inputarc;


    public Petrinet_Place(
    ) {
        super(
        );
    }



    public Petrinet_OutputArc getPetrinet_outputarc() {
        return petrinet_outputarc;
    }

    public void setPetrinet_outputarc(Petrinet_OutputArc petrinet_outputarc) {
        this.petrinet_outputarc = petrinet_outputarc;
    }
    public Petrinet_InputArc getPetrinet_inputarc() {
        return petrinet_inputarc;
    }

    public void setPetrinet_inputarc(Petrinet_InputArc petrinet_inputarc) {
        this.petrinet_inputarc = petrinet_inputarc;
    }

}