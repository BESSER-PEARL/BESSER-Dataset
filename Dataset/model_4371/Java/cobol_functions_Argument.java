





import java.util.List;
import java.util.ArrayList;

public class cobol_functions_Argument  {






    private List<PrimaryOperand> primaryoperands;


    public cobol_functions_Argument(
    ) {
        this.primaryoperands = new ArrayList<>();
    }

    public cobol_functions_Argument(
        ArrayList<PrimaryOperand> primaryoperands    ) {
        this.primaryoperands = primaryoperands;
    }


    public List<PrimaryOperand> getPrimaryoperands() {
        return primaryoperands;
    }

    public void addPrimaryoperand(Primaryoperand primaryoperand) {
        this.primaryoperands.add(primaryoperand);
    }

}