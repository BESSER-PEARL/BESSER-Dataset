





import java.util.List;
import java.util.ArrayList;

public class xpand3_declaration_JavaExtension extends AbstractNamedDeclaration {






    private declaration_xpand3_Identifier declaration_xpand3_identifier;




    private declaration_xpand3_Identifier declaration_xpand3_identifier;




    private List<declaration_xpand3_Identifier> declaration_xpand3_identifiers;


    public xpand3_declaration_JavaExtension(
    ) {
        super(
        );
        this.declaration_xpand3_identifiers = new ArrayList<>();
    }

    public xpand3_declaration_JavaExtension(
        ArrayList<declaration_xpand3_Identifier> declaration_xpand3_identifiers    ) {
        this.declaration_xpand3_identifiers = declaration_xpand3_identifiers;
    }


    public declaration_xpand3_Identifier getDeclaration_xpand3_identifier() {
        return declaration_xpand3_identifier;
    }

    public void setDeclaration_xpand3_identifier(declaration_xpand3_Identifier declaration_xpand3_identifier) {
        this.declaration_xpand3_identifier = declaration_xpand3_identifier;
    }
    public declaration_xpand3_Identifier getDeclaration_xpand3_identifier() {
        return declaration_xpand3_identifier;
    }

    public void setDeclaration_xpand3_identifier(declaration_xpand3_Identifier declaration_xpand3_identifier) {
        this.declaration_xpand3_identifier = declaration_xpand3_identifier;
    }
    public List<declaration_xpand3_Identifier> getDeclaration_xpand3_identifiers() {
        return declaration_xpand3_identifiers;
    }

    public void addDeclaration_xpand3_identifier(Declaration_xpand3_identifier declaration_xpand3_identifier) {
        this.declaration_xpand3_identifiers.add(declaration_xpand3_identifier);
    }

}