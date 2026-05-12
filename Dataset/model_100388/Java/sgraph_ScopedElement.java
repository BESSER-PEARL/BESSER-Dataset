





import java.util.List;
import java.util.ArrayList;

public class sgraph_ScopedElement  {

    private String namespace;





    private List<sgraph_Scope> sgraph_scopes;


    public sgraph_ScopedElement(
        String namespace    ) {
        this.namespace = namespace;
        this.sgraph_scopes = new ArrayList<>();
    }

    public sgraph_ScopedElement(
        String namespace        ArrayList<sgraph_Scope> sgraph_scopes    ) {
        this.namespace = namespace;
        this.sgraph_scopes = sgraph_scopes;
    }

    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }

    public List<sgraph_Scope> getSgraph_scopes() {
        return sgraph_scopes;
    }

    public void addSgraph_scope(Sgraph_scope sgraph_scope) {
        this.sgraph_scopes.add(sgraph_scope);
    }

}