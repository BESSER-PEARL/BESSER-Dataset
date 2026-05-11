





import java.util.List;
import java.util.ArrayList;

public class uppaal_templates_Synchronization  {

    private String kind;





    private IdentifierExpression identifierexpression;


    public uppaal_templates_Synchronization(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public IdentifierExpression getIdentifierexpression() {
        return identifierexpression;
    }

    public void setIdentifierexpression(IdentifierExpression identifierexpression) {
        this.identifierexpression = identifierexpression;
    }

}