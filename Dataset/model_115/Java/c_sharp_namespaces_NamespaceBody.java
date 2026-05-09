





import java.util.List;
import java.util.ArrayList;

public class c_sharp_namespaces_NamespaceBody  {






    private List<NamespaceMemberDeclaration> namespacememberdeclarations;




    private List<UsingDirective> usingdirectives;


    public c_sharp_namespaces_NamespaceBody(
    ) {
        this.namespacememberdeclarations = new ArrayList<>();
        this.usingdirectives = new ArrayList<>();
    }

    public c_sharp_namespaces_NamespaceBody(
        ArrayList<NamespaceMemberDeclaration> namespacememberdeclarations,        ArrayList<UsingDirective> usingdirectives    ) {
        this.namespacememberdeclarations = namespacememberdeclarations;
        this.usingdirectives = usingdirectives;
    }


    public List<NamespaceMemberDeclaration> getNamespacememberdeclarations() {
        return namespacememberdeclarations;
    }

    public void addNamespacememberdeclaration(Namespacememberdeclaration namespacememberdeclaration) {
        this.namespacememberdeclarations.add(namespacememberdeclaration);
    }
    public List<UsingDirective> getUsingdirectives() {
        return usingdirectives;
    }

    public void addUsingdirective(Usingdirective usingdirective) {
        this.usingdirectives.add(usingdirective);
    }

}