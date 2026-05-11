





import java.util.List;
import java.util.ArrayList;

public class b_Sees  {






    private List<b_Abstraction> b_abstractions;




    private b_Abstraction b_abstraction;


    public b_Sees(
    ) {
        this.b_abstractions = new ArrayList<>();
    }

    public b_Sees(
        ArrayList<b_Abstraction> b_abstractions    ) {
        this.b_abstractions = b_abstractions;
    }


    public List<b_Abstraction> getB_abstractions() {
        return b_abstractions;
    }

    public void addB_abstraction(B_abstraction b_abstraction) {
        this.b_abstractions.add(b_abstraction);
    }
    public b_Abstraction getB_abstraction() {
        return b_abstraction;
    }

    public void setB_abstraction(b_Abstraction b_abstraction) {
        this.b_abstraction = b_abstraction;
    }

}