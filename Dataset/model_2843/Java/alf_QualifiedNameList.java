





import java.util.List;
import java.util.ArrayList;

public class alf_QualifiedNameList  {






    private alf_AcceptClause alf_acceptclause;




    private List<alf_QualifiedNameWithBinding> alf_qualifiednamewithbindings;


    public alf_QualifiedNameList(
    ) {
        this.alf_qualifiednamewithbindings = new ArrayList<>();
    }

    public alf_QualifiedNameList(
        ArrayList<alf_QualifiedNameWithBinding> alf_qualifiednamewithbindings    ) {
        this.alf_qualifiednamewithbindings = alf_qualifiednamewithbindings;
    }


    public alf_AcceptClause getAlf_acceptclause() {
        return alf_acceptclause;
    }

    public void setAlf_acceptclause(alf_AcceptClause alf_acceptclause) {
        this.alf_acceptclause = alf_acceptclause;
    }
    public List<alf_QualifiedNameWithBinding> getAlf_qualifiednamewithbindings() {
        return alf_qualifiednamewithbindings;
    }

    public void addAlf_qualifiednamewithbinding(Alf_qualifiednamewithbinding alf_qualifiednamewithbinding) {
        this.alf_qualifiednamewithbindings.add(alf_qualifiednamewithbinding);
    }

}