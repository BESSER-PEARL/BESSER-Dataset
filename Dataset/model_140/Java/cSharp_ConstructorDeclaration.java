





import java.util.List;
import java.util.ArrayList;

public class cSharp_ConstructorDeclaration  {

    private String constModifier;





    private cSharp_ClassMemberDeclaration csharp_classmemberdeclaration;


    public cSharp_ConstructorDeclaration(
        String constModifier    ) {
        this.constModifier = constModifier;
    }


    public String getConstmodifier() {
        return constModifier;
    }

    public void setConstmodifier(String constModifier) {
        this.constModifier = constModifier;
    }

    public cSharp_ClassMemberDeclaration getCsharp_classmemberdeclaration() {
        return csharp_classmemberdeclaration;
    }

    public void setCsharp_classmemberdeclaration(cSharp_ClassMemberDeclaration csharp_classmemberdeclaration) {
        this.csharp_classmemberdeclaration = csharp_classmemberdeclaration;
    }

}