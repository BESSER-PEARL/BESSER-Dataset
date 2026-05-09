





import java.util.List;
import java.util.ArrayList;

public class extendedPetriNets_Place extends GenericPlace {






    private extendedPetriNets_OutputArc extendedpetrinets_outputarc;




    private extendedPetriNets_InputArc extendedpetrinets_inputarc;


    public extendedPetriNets_Place(
    ) {
        super(
        );
    }



    public extendedPetriNets_OutputArc getExtendedpetrinets_outputarc() {
        return extendedpetrinets_outputarc;
    }

    public void setExtendedpetrinets_outputarc(extendedPetriNets_OutputArc extendedpetrinets_outputarc) {
        this.extendedpetrinets_outputarc = extendedpetrinets_outputarc;
    }
    public extendedPetriNets_InputArc getExtendedpetrinets_inputarc() {
        return extendedpetrinets_inputarc;
    }

    public void setExtendedpetrinets_inputarc(extendedPetriNets_InputArc extendedpetrinets_inputarc) {
        this.extendedpetrinets_inputarc = extendedpetrinets_inputarc;
    }

}