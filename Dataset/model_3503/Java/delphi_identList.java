





import java.util.List;
import java.util.ArrayList;

public class delphi_identList extends objFieldList, classHeritage {






    private delphi_containsClause delphi_containsclause;




    private delphi_requiresClause delphi_requiresclause;




    private List<delphi_ident> delphi_idents;




    private delphi_program delphi_program;




    private delphi_usesClause delphi_usesclause;


    public delphi_identList(
    ) {
        super(
        );
        this.delphi_idents = new ArrayList<>();
    }

    public delphi_identList(
        ArrayList<delphi_ident> delphi_idents    ) {
        this.delphi_idents = delphi_idents;
    }


    public delphi_containsClause getDelphi_containsclause() {
        return delphi_containsclause;
    }

    public void setDelphi_containsclause(delphi_containsClause delphi_containsclause) {
        this.delphi_containsclause = delphi_containsclause;
    }
    public delphi_requiresClause getDelphi_requiresclause() {
        return delphi_requiresclause;
    }

    public void setDelphi_requiresclause(delphi_requiresClause delphi_requiresclause) {
        this.delphi_requiresclause = delphi_requiresclause;
    }
    public List<delphi_ident> getDelphi_idents() {
        return delphi_idents;
    }

    public void addDelphi_ident(Delphi_ident delphi_ident) {
        this.delphi_idents.add(delphi_ident);
    }
    public delphi_program getDelphi_program() {
        return delphi_program;
    }

    public void setDelphi_program(delphi_program delphi_program) {
        this.delphi_program = delphi_program;
    }
    public delphi_usesClause getDelphi_usesclause() {
        return delphi_usesclause;
    }

    public void setDelphi_usesclause(delphi_usesClause delphi_usesclause) {
        this.delphi_usesclause = delphi_usesclause;
    }

}