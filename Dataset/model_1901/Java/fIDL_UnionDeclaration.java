





import java.util.List;
import java.util.ArrayList;

public class fIDL_UnionDeclaration extends Declaration {






    private List<fIDL_ConstDeclaration> fidl_constdeclarations;


    public fIDL_UnionDeclaration(
    ) {
        super(
        );
        this.fidl_constdeclarations = new ArrayList<>();
    }

    public fIDL_UnionDeclaration(
        ArrayList<fIDL_ConstDeclaration> fidl_constdeclarations    ) {
        this.fidl_constdeclarations = fidl_constdeclarations;
    }


    public List<fIDL_ConstDeclaration> getFidl_constdeclarations() {
        return fidl_constdeclarations;
    }

    public void addFidl_constdeclaration(Fidl_constdeclaration fidl_constdeclaration) {
        this.fidl_constdeclarations.add(fidl_constdeclaration);
    }

}