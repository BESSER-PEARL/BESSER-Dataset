





import java.util.List;
import java.util.ArrayList;

public class xpand3_declaration_Extension extends AbstractNamedDeclaration {

    private boolean cached;





    private declaration_xpand3_Identifier declaration_xpand3_identifier;




    private AbstractExpression abstractexpression;


    public xpand3_declaration_Extension(
        boolean cached    ) {
        super(
        );
        this.cached = cached;
    }


    public boolean getCached() {
        return cached;
    }

    public void setCached(boolean cached) {
        this.cached = cached;
    }

    public declaration_xpand3_Identifier getDeclaration_xpand3_identifier() {
        return declaration_xpand3_identifier;
    }

    public void setDeclaration_xpand3_identifier(declaration_xpand3_Identifier declaration_xpand3_identifier) {
        this.declaration_xpand3_identifier = declaration_xpand3_identifier;
    }
    public AbstractExpression getAbstractexpression() {
        return abstractexpression;
    }

    public void setAbstractexpression(AbstractExpression abstractexpression) {
        this.abstractexpression = abstractexpression;
    }

}