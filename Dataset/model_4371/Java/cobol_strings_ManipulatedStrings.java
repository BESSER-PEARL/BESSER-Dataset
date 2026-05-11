





import java.util.List;
import java.util.ArrayList;

public class cobol_strings_ManipulatedStrings extends String {






    private PrimaryOperand primaryoperand;




    private List<PrimaryOperand> primaryoperands;


    public cobol_strings_ManipulatedStrings(
    ) {
        super(
        );
        this.primaryoperands = new ArrayList<>();
    }

    public cobol_strings_ManipulatedStrings(
        ArrayList<PrimaryOperand> primaryoperands    ) {
        this.primaryoperands = primaryoperands;
    }


    public PrimaryOperand getPrimaryoperand() {
        return primaryoperand;
    }

    public void setPrimaryoperand(PrimaryOperand primaryoperand) {
        this.primaryoperand = primaryoperand;
    }
    public List<PrimaryOperand> getPrimaryoperands() {
        return primaryoperands;
    }

    public void addPrimaryoperand(Primaryoperand primaryoperand) {
        this.primaryoperands.add(primaryoperand);
    }

}