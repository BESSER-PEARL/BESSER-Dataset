





import java.util.List;
import java.util.ArrayList;

public class fIDL_InterfaceDeclaration extends Declaration {






    private List<fIDL_InterfaceMember> fidl_interfacemembers;




    private List<fIDL_InterfaceDeclaration> fidl_interfacedeclarations;


    public fIDL_InterfaceDeclaration(
    ) {
        super(
        );
        this.fidl_interfacemembers = new ArrayList<>();
        this.fidl_interfacedeclarations = new ArrayList<>();
    }

    public fIDL_InterfaceDeclaration(
        ArrayList<fIDL_InterfaceMember> fidl_interfacemembers,        ArrayList<fIDL_InterfaceDeclaration> fidl_interfacedeclarations    ) {
        this.fidl_interfacemembers = fidl_interfacemembers;
        this.fidl_interfacedeclarations = fidl_interfacedeclarations;
    }


    public List<fIDL_InterfaceMember> getFidl_interfacemembers() {
        return fidl_interfacemembers;
    }

    public void addFidl_interfacemember(Fidl_interfacemember fidl_interfacemember) {
        this.fidl_interfacemembers.add(fidl_interfacemember);
    }
    public List<fIDL_InterfaceDeclaration> getFidl_interfacedeclarations() {
        return fidl_interfacedeclarations;
    }

    public void addFidl_interfacedeclaration(Fidl_interfacedeclaration fidl_interfacedeclaration) {
        this.fidl_interfacedeclarations.add(fidl_interfacedeclaration);
    }

}