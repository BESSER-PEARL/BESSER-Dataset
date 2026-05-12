





import java.util.List;
import java.util.ArrayList;

public class PetriNetMM2_Place extends GenericPT {

    private String name;
    private int relevance;



    public PetriNetMM2_Place(
        String name,        int relevance    ) {
        super(
        );
        this.name = name;
        this.relevance = relevance;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getRelevance() {
        return relevance;
    }

    public void setRelevance(int relevance) {
        this.relevance = relevance;
    }


}