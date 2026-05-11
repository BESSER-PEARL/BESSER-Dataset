





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_Jump extends Statement {






    private List<ProcedureRangeLabel> procedurerangelabels;


    public cobol_statements_Jump(
    ) {
        super(
        );
        this.procedurerangelabels = new ArrayList<>();
    }

    public cobol_statements_Jump(
        ArrayList<ProcedureRangeLabel> procedurerangelabels    ) {
        this.procedurerangelabels = procedurerangelabels;
    }


    public List<ProcedureRangeLabel> getProcedurerangelabels() {
        return procedurerangelabels;
    }

    public void addProcedurerangelabel(Procedurerangelabel procedurerangelabel) {
        this.procedurerangelabels.add(procedurerangelabel);
    }

}