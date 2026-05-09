





import java.util.List;
import java.util.ArrayList;

public class PetriNets_Place extends Node {

    private int tokens;





    private PetriNets_PTArc petrinets_ptarc;




    private PetriNets_TPArc petrinets_tparc;


    public PetriNets_Place(
        int tokens    ) {
        super(
        );
        this.tokens = tokens;
    }


    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }

    public PetriNets_PTArc getPetrinets_ptarc() {
        return petrinets_ptarc;
    }

    public void setPetrinets_ptarc(PetriNets_PTArc petrinets_ptarc) {
        this.petrinets_ptarc = petrinets_ptarc;
    }
    public PetriNets_TPArc getPetrinets_tparc() {
        return petrinets_tparc;
    }

    public void setPetrinets_tparc(PetriNets_TPArc petrinets_tparc) {
        this.petrinets_tparc = petrinets_tparc;
    }

}