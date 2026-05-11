





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgDialog extends TrgSession {






    private List<TrgDeclaration> trgdeclarations;


    public jointPackage_CPL2SPL_TrgDialog(
    ) {
        super(
        );
        this.trgdeclarations = new ArrayList<>();
    }

    public jointPackage_CPL2SPL_TrgDialog(
        ArrayList<TrgDeclaration> trgdeclarations    ) {
        this.trgdeclarations = trgdeclarations;
    }


    public List<TrgDeclaration> getTrgdeclarations() {
        return trgdeclarations;
    }

    public void addTrgdeclaration(Trgdeclaration trgdeclaration) {
        this.trgdeclarations.add(trgdeclaration);
    }

}