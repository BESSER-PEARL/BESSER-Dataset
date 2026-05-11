





import java.util.List;
import java.util.ArrayList;

public class alf_QualifiedNameList  {






    private alf_RedefinitionClause alf_redefinitionclause;




    private List<alf_QualifiedNameWithBinding> alf_qualifiednamewithbindings;


    public alf_QualifiedNameList(
    ) {
        this.alf_qualifiednamewithbindings = new ArrayList<>();
    }

    public alf_QualifiedNameList(
        ArrayList<alf_QualifiedNameWithBinding> alf_qualifiednamewithbindings    ) {
        this.alf_qualifiednamewithbindings = alf_qualifiednamewithbindings;
    }


    public alf_RedefinitionClause getAlf_redefinitionclause() {
        return alf_redefinitionclause;
    }

    public void setAlf_redefinitionclause(alf_RedefinitionClause alf_redefinitionclause) {
        this.alf_redefinitionclause = alf_redefinitionclause;
    }
    public List<alf_QualifiedNameWithBinding> getAlf_qualifiednamewithbindings() {
        return alf_qualifiednamewithbindings;
    }

    public void addAlf_qualifiednamewithbinding(Alf_qualifiednamewithbinding alf_qualifiednamewithbinding) {
        this.alf_qualifiednamewithbindings.add(alf_qualifiednamewithbinding);
    }

}