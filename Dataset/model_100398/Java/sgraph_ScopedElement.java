





import java.util.List;
import java.util.ArrayList;

public class sgraph_ScopedElement  {






    private List<sgraph_Scope> sgraph_scopes;


    public sgraph_ScopedElement(
    ) {
        this.sgraph_scopes = new ArrayList<>();
    }

    public sgraph_ScopedElement(
        ArrayList<sgraph_Scope> sgraph_scopes    ) {
        this.sgraph_scopes = sgraph_scopes;
    }


    public List<sgraph_Scope> getSgraph_scopes() {
        return sgraph_scopes;
    }

    public void addSgraph_scope(Sgraph_scope sgraph_scope) {
        this.sgraph_scopes.add(sgraph_scope);
    }

}