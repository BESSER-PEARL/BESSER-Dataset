





import java.util.List;
import java.util.ArrayList;

public class cSharpArchId_Modifier extends ASTNode {

    private String visibility;
    private boolean static;
    private String modifier;
    private String inheritance;





    private cSharpArchId_BodyDeclaration csharparchid_bodydeclaration;




    private cSharpArchId_BodyDeclaration csharparchid_bodydeclaration;


    public cSharpArchId_Modifier(
        String visibility,        boolean static,        String modifier,        String inheritance    ) {
        super(
        );
        this.visibility = visibility;
        this.static = static;
        this.modifier = modifier;
        this.inheritance = inheritance;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }

    public cSharpArchId_BodyDeclaration getCsharparchid_bodydeclaration() {
        return csharparchid_bodydeclaration;
    }

    public void setCsharparchid_bodydeclaration(cSharpArchId_BodyDeclaration csharparchid_bodydeclaration) {
        this.csharparchid_bodydeclaration = csharparchid_bodydeclaration;
    }
    public cSharpArchId_BodyDeclaration getCsharparchid_bodydeclaration() {
        return csharparchid_bodydeclaration;
    }

    public void setCsharparchid_bodydeclaration(cSharpArchId_BodyDeclaration csharparchid_bodydeclaration) {
        this.csharparchid_bodydeclaration = csharparchid_bodydeclaration;
    }

}