





import java.util.List;
import java.util.ArrayList;

public class cSharp_OperatorDeclaration  {

    private String opModifier;





    private cSharp_ClassMemberDeclaration csharp_classmemberdeclaration;


    public cSharp_OperatorDeclaration(
        String opModifier    ) {
        this.opModifier = opModifier;
    }


    public String getOpmodifier() {
        return opModifier;
    }

    public void setOpmodifier(String opModifier) {
        this.opModifier = opModifier;
    }

    public cSharp_ClassMemberDeclaration getCsharp_classmemberdeclaration() {
        return csharp_classmemberdeclaration;
    }

    public void setCsharp_classmemberdeclaration(cSharp_ClassMemberDeclaration csharp_classmemberdeclaration) {
        this.csharp_classmemberdeclaration = csharp_classmemberdeclaration;
    }

}