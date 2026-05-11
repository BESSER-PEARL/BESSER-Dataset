





import java.util.List;
import java.util.ArrayList;

public class cool_IdentifiableElement  {

    private String name;





    private cool_IdentifierRefExpression cool_identifierrefexpression;


    public cool_IdentifiableElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cool_IdentifierRefExpression getCool_identifierrefexpression() {
        return cool_identifierrefexpression;
    }

    public void setCool_identifierrefexpression(cool_IdentifierRefExpression cool_identifierrefexpression) {
        this.cool_identifierrefexpression = cool_identifierrefexpression;
    }

}