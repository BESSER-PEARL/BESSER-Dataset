





import java.util.List;
import java.util.ArrayList;

public class cSharpArchId_Enumeration extends Type {






    private cSharpArchId_Namespace csharparchid_namespace;




    private List<cSharpArchId_EnumerationLiteral> csharparchid_enumerationliterals;


    public cSharpArchId_Enumeration(
    ) {
        super(
        );
        this.csharparchid_enumerationliterals = new ArrayList<>();
    }

    public cSharpArchId_Enumeration(
        ArrayList<cSharpArchId_EnumerationLiteral> csharparchid_enumerationliterals    ) {
        this.csharparchid_enumerationliterals = csharparchid_enumerationliterals;
    }


    public cSharpArchId_Namespace getCsharparchid_namespace() {
        return csharparchid_namespace;
    }

    public void setCsharparchid_namespace(cSharpArchId_Namespace csharparchid_namespace) {
        this.csharparchid_namespace = csharparchid_namespace;
    }
    public List<cSharpArchId_EnumerationLiteral> getCsharparchid_enumerationliterals() {
        return csharparchid_enumerationliterals;
    }

    public void addCsharparchid_enumerationliteral(Csharparchid_enumerationliteral csharparchid_enumerationliteral) {
        this.csharparchid_enumerationliterals.add(csharparchid_enumerationliteral);
    }

}