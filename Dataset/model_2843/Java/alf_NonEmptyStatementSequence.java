





import java.util.List;
import java.util.ArrayList;

public class alf_NonEmptyStatementSequence  {






    private List<alf_DocumentedStatement> alf_documentedstatements;




    private alf_SwitchClause alf_switchclause;




    private alf_SwitchDefaultClause alf_switchdefaultclause;


    public alf_NonEmptyStatementSequence(
    ) {
        this.alf_documentedstatements = new ArrayList<>();
    }

    public alf_NonEmptyStatementSequence(
        ArrayList<alf_DocumentedStatement> alf_documentedstatements    ) {
        this.alf_documentedstatements = alf_documentedstatements;
    }


    public List<alf_DocumentedStatement> getAlf_documentedstatements() {
        return alf_documentedstatements;
    }

    public void addAlf_documentedstatement(Alf_documentedstatement alf_documentedstatement) {
        this.alf_documentedstatements.add(alf_documentedstatement);
    }
    public alf_SwitchClause getAlf_switchclause() {
        return alf_switchclause;
    }

    public void setAlf_switchclause(alf_SwitchClause alf_switchclause) {
        this.alf_switchclause = alf_switchclause;
    }
    public alf_SwitchDefaultClause getAlf_switchdefaultclause() {
        return alf_switchdefaultclause;
    }

    public void setAlf_switchdefaultclause(alf_SwitchDefaultClause alf_switchdefaultclause) {
        this.alf_switchdefaultclause = alf_switchdefaultclause;
    }

}