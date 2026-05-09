





import java.util.List;
import java.util.ArrayList;

public class cSharp_QualifiedIdentifierList  {






    private cSharp_BuiltInClassType csharp_builtinclasstype;




    private List<cSharp_QualifiedIdentifier> csharp_qualifiedidentifiers;




    private cSharp_QualifiedIdentifier csharp_qualifiedidentifier;


    public cSharp_QualifiedIdentifierList(
    ) {
        this.csharp_qualifiedidentifiers = new ArrayList<>();
    }

    public cSharp_QualifiedIdentifierList(
        ArrayList<cSharp_QualifiedIdentifier> csharp_qualifiedidentifiers    ) {
        this.csharp_qualifiedidentifiers = csharp_qualifiedidentifiers;
    }


    public cSharp_BuiltInClassType getCsharp_builtinclasstype() {
        return csharp_builtinclasstype;
    }

    public void setCsharp_builtinclasstype(cSharp_BuiltInClassType csharp_builtinclasstype) {
        this.csharp_builtinclasstype = csharp_builtinclasstype;
    }
    public List<cSharp_QualifiedIdentifier> getCsharp_qualifiedidentifiers() {
        return csharp_qualifiedidentifiers;
    }

    public void addCsharp_qualifiedidentifier(Csharp_qualifiedidentifier csharp_qualifiedidentifier) {
        this.csharp_qualifiedidentifiers.add(csharp_qualifiedidentifier);
    }
    public cSharp_QualifiedIdentifier getCsharp_qualifiedidentifier() {
        return csharp_qualifiedidentifier;
    }

    public void setCsharp_qualifiedidentifier(cSharp_QualifiedIdentifier csharp_qualifiedidentifier) {
        this.csharp_qualifiedidentifier = csharp_qualifiedidentifier;
    }

}