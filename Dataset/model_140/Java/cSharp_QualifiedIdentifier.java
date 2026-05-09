





import java.util.List;
import java.util.ArrayList;

public class cSharp_QualifiedIdentifier  {






    private cSharp_UsingDirective csharp_usingdirective;




    private cSharp_Identifier csharp_identifier;




    private List<cSharp_Identifier> csharp_identifiers;


    public cSharp_QualifiedIdentifier(
    ) {
        this.csharp_identifiers = new ArrayList<>();
    }

    public cSharp_QualifiedIdentifier(
        ArrayList<cSharp_Identifier> csharp_identifiers    ) {
        this.csharp_identifiers = csharp_identifiers;
    }


    public cSharp_UsingDirective getCsharp_usingdirective() {
        return csharp_usingdirective;
    }

    public void setCsharp_usingdirective(cSharp_UsingDirective csharp_usingdirective) {
        this.csharp_usingdirective = csharp_usingdirective;
    }
    public cSharp_Identifier getCsharp_identifier() {
        return csharp_identifier;
    }

    public void setCsharp_identifier(cSharp_Identifier csharp_identifier) {
        this.csharp_identifier = csharp_identifier;
    }
    public List<cSharp_Identifier> getCsharp_identifiers() {
        return csharp_identifiers;
    }

    public void addCsharp_identifier(Csharp_identifier csharp_identifier) {
        this.csharp_identifiers.add(csharp_identifier);
    }

}