





import java.util.List;
import java.util.ArrayList;

public class cSharp_ClassDeclaration  {

    private String classModifier;





    private cSharp_Identifier csharp_identifier;


    public cSharp_ClassDeclaration(
        String classModifier    ) {
        this.classModifier = classModifier;
    }


    public String getClassmodifier() {
        return classModifier;
    }

    public void setClassmodifier(String classModifier) {
        this.classModifier = classModifier;
    }

    public cSharp_Identifier getCsharp_identifier() {
        return csharp_identifier;
    }

    public void setCsharp_identifier(cSharp_Identifier csharp_identifier) {
        this.csharp_identifier = csharp_identifier;
    }

}