





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_Choice extends ActionStep {






    private List<CaseItem> caseitems;


    public core_actionstep_Choice(
    ) {
        super(
        );
        this.caseitems = new ArrayList<>();
    }

    public core_actionstep_Choice(
        ArrayList<CaseItem> caseitems    ) {
        this.caseitems = caseitems;
    }


    public List<CaseItem> getCaseitems() {
        return caseitems;
    }

    public void addCaseitem(Caseitem caseitem) {
        this.caseitems.add(caseitem);
    }

}