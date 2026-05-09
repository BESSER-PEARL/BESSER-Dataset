





import java.util.List;
import java.util.ArrayList;

public class cSharp_IndexerDeclaration  {

    private String idModifier;





    private cSharp_AccessorDeclarations csharp_accessordeclarations;




    private cSharp_ClassMemberDeclaration csharp_classmemberdeclaration;


    public cSharp_IndexerDeclaration(
        String idModifier    ) {
        this.idModifier = idModifier;
    }


    public String getIdmodifier() {
        return idModifier;
    }

    public void setIdmodifier(String idModifier) {
        this.idModifier = idModifier;
    }

    public cSharp_AccessorDeclarations getCsharp_accessordeclarations() {
        return csharp_accessordeclarations;
    }

    public void setCsharp_accessordeclarations(cSharp_AccessorDeclarations csharp_accessordeclarations) {
        this.csharp_accessordeclarations = csharp_accessordeclarations;
    }
    public cSharp_ClassMemberDeclaration getCsharp_classmemberdeclaration() {
        return csharp_classmemberdeclaration;
    }

    public void setCsharp_classmemberdeclaration(cSharp_ClassMemberDeclaration csharp_classmemberdeclaration) {
        this.csharp_classmemberdeclaration = csharp_classmemberdeclaration;
    }

}