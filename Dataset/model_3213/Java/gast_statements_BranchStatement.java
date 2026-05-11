





import java.util.List;
import java.util.ArrayList;

public class gast_statements_BranchStatement extends Statement {






    private List<Branch> branchs;


    public gast_statements_BranchStatement(
    ) {
        super(
        );
        this.branchs = new ArrayList<>();
    }

    public gast_statements_BranchStatement(
        ArrayList<Branch> branchs    ) {
        this.branchs = branchs;
    }


    public List<Branch> getBranchs() {
        return branchs;
    }

    public void addBranch(Branch branch) {
        this.branchs.add(branch);
    }

}