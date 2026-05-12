





import java.util.List;
import java.util.ArrayList;

public class PetriNetMM2_Transition extends GenericPT {

    private int relevance;
    private String name;



    public PetriNetMM2_Transition(
        int relevance,        String name    ) {
        super(
        );
        this.relevance = relevance;
        this.name = name;
    }


    public int getRelevance() {
        return relevance;
    }

    public void setRelevance(int relevance) {
        this.relevance = relevance;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}