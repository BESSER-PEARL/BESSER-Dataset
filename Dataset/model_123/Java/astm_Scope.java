





import java.util.List;
import java.util.ArrayList;

public class astm_Scope extends GASTMSemanticObject {






    private List<astm_Scope> astm_scopes;


    public astm_Scope(
    ) {
        super(
        );
        this.astm_scopes = new ArrayList<>();
    }

    public astm_Scope(
        ArrayList<astm_Scope> astm_scopes    ) {
        this.astm_scopes = astm_scopes;
    }


    public List<astm_Scope> getAstm_scopes() {
        return astm_scopes;
    }

    public void addAstm_scope(Astm_scope astm_scope) {
        this.astm_scopes.add(astm_scope);
    }

}