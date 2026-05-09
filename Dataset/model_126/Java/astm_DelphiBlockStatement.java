





import java.util.List;
import java.util.ArrayList;

public class astm_DelphiBlockStatement extends BlockStatement {






    private List<astm_NamedTypeReference> astm_namedtypereferences;


    public astm_DelphiBlockStatement(
    ) {
        super(
        );
        this.astm_namedtypereferences = new ArrayList<>();
    }

    public astm_DelphiBlockStatement(
        ArrayList<astm_NamedTypeReference> astm_namedtypereferences    ) {
        this.astm_namedtypereferences = astm_namedtypereferences;
    }


    public List<astm_NamedTypeReference> getAstm_namedtypereferences() {
        return astm_namedtypereferences;
    }

    public void addAstm_namedtypereference(Astm_namedtypereference astm_namedtypereference) {
        this.astm_namedtypereferences.add(astm_namedtypereference);
    }

}