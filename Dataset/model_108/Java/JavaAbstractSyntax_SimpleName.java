





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_SimpleName extends Name {

    private String identifier;
    private String declaration;



    public JavaAbstractSyntax_SimpleName(
        String identifier,        String declaration    ) {
        super(
        );
        this.identifier = identifier;
        this.declaration = declaration;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getDeclaration() {
        return declaration;
    }

    public void setDeclaration(String declaration) {
        this.declaration = declaration;
    }


}