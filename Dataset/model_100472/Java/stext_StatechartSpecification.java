





import java.util.List;
import java.util.ArrayList;

public class stext_StatechartSpecification  {

    private String namespace;





    private List<stext_Scope> stext_scopes;




    private stext_StatechartRoot stext_statechartroot;


    public stext_StatechartSpecification(
        String namespace    ) {
        this.namespace = namespace;
        this.stext_scopes = new ArrayList<>();
    }

    public stext_StatechartSpecification(
        String namespace        ArrayList<stext_Scope> stext_scopes    ) {
        this.namespace = namespace;
        this.stext_scopes = stext_scopes;
    }

    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }

    public List<stext_Scope> getStext_scopes() {
        return stext_scopes;
    }

    public void addStext_scope(Stext_scope stext_scope) {
        this.stext_scopes.add(stext_scope);
    }
    public stext_StatechartRoot getStext_statechartroot() {
        return stext_statechartroot;
    }

    public void setStext_statechartroot(stext_StatechartRoot stext_statechartroot) {
        this.stext_statechartroot = stext_statechartroot;
    }

}