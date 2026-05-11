





import java.util.List;
import java.util.ArrayList;

public class b_Imports  {






    private List<b_Abstraction> b_abstractions;




    private b_Implementation b_implementation;


    public b_Imports(
    ) {
        this.b_abstractions = new ArrayList<>();
    }

    public b_Imports(
        ArrayList<b_Abstraction> b_abstractions    ) {
        this.b_abstractions = b_abstractions;
    }


    public List<b_Abstraction> getB_abstractions() {
        return b_abstractions;
    }

    public void addB_abstraction(B_abstraction b_abstraction) {
        this.b_abstractions.add(b_abstraction);
    }
    public b_Implementation getB_implementation() {
        return b_implementation;
    }

    public void setB_implementation(b_Implementation b_implementation) {
        this.b_implementation = b_implementation;
    }

}