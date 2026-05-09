





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Node {






    private petrinet_InputArc petrinet_inputarc;




    private petrinet_OutputArc petrinet_outputarc;


    public petrinet_Place(
    ) {
        super(
        );
    }



    public petrinet_InputArc getPetrinet_inputarc() {
        return petrinet_inputarc;
    }

    public void setPetrinet_inputarc(petrinet_InputArc petrinet_inputarc) {
        this.petrinet_inputarc = petrinet_inputarc;
    }
    public petrinet_OutputArc getPetrinet_outputarc() {
        return petrinet_outputarc;
    }

    public void setPetrinet_outputarc(petrinet_OutputArc petrinet_outputarc) {
        this.petrinet_outputarc = petrinet_outputarc;
    }

}