





import java.util.List;
import java.util.ArrayList;

public class eol_EOLLibraryModule extends EOLElement {

    private String name;





    private List<eol_ModelDeclarationStatement> eol_modeldeclarationstatements;


    public eol_EOLLibraryModule(
        String name    ) {
        super(
        );
        this.name = name;
        this.eol_modeldeclarationstatements = new ArrayList<>();
    }

    public eol_EOLLibraryModule(
        String name        ArrayList<eol_ModelDeclarationStatement> eol_modeldeclarationstatements    ) {
        this.name = name;
        this.eol_modeldeclarationstatements = eol_modeldeclarationstatements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<eol_ModelDeclarationStatement> getEol_modeldeclarationstatements() {
        return eol_modeldeclarationstatements;
    }

    public void addEol_modeldeclarationstatement(Eol_modeldeclarationstatement eol_modeldeclarationstatement) {
        this.eol_modeldeclarationstatements.add(eol_modeldeclarationstatement);
    }

}