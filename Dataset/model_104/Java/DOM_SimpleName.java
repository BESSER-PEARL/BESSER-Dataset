





import java.util.List;
import java.util.ArrayList;

public class DOM_SimpleName extends Name {

    private String declaration;
    private String identifier;



    public DOM_SimpleName(
        String declaration,        String identifier    ) {
        super(
        );
        this.declaration = declaration;
        this.identifier = identifier;
    }


    public String getDeclaration() {
        return declaration;
    }

    public void setDeclaration(String declaration) {
        this.declaration = declaration;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}