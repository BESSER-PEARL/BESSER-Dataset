





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_Cancel extends Statement {






    private List<PrimaryOperand> primaryoperands;


    public cobol_statements_Cancel(
    ) {
        super(
        );
        this.primaryoperands = new ArrayList<>();
    }

    public cobol_statements_Cancel(
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