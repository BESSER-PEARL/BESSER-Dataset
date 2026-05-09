





import java.util.List;
import java.util.ArrayList;

public class cSharp_NamespaceBody  {






    private List<cSharp_NamespaceMemberDeclaration> csharp_namespacememberdeclarations;




    private List<cSharp_UsingDirective> csharp_usingdirectives;


    public cSharp_NamespaceBody(
    ) {
        this.csharp_namespacememberdeclarations = new ArrayList<>();
        this.csharp_usingdirectives = new ArrayList<>();
    }

    public cSharp_NamespaceBody(
        ArrayList<cSharp_NamespaceMemberDeclaration> csharp_namespacememberdeclarations,        ArrayList<cSharp_UsingDirective> csharp_usingdirectives    ) {
        this.csharp_namespacememberdeclarations = csharp_namespacememberdeclarations;
        this.csharp_usingdirectives = csharp_usingdirectives;
    }


    public List<cSharp_NamespaceMemberDeclaration> getCsharp_namespacememberdeclarations() {
        return csharp_namespacememberdeclarations;
    }

    public void addCsharp_namespacememberdeclaration(Csharp_namespacememberdeclaration csharp_namespacememberdeclaration) {
        this.csharp_namespacememberdeclarations.add(csharp_namespacememberdeclaration);
    }
    public List<cSharp_UsingDirective> getCsharp_usingdirectives() {
        return csharp_usingdirectives;
    }

    public void addCsharp_usingdirective(Csharp_usingdirective csharp_usingdirective) {
        this.csharp_usingdirectives.add(csharp_usingdirective);
    }

}