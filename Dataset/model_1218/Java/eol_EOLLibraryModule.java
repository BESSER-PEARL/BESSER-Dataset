





import java.util.List;
import java.util.ArrayList;

public class eol_EOLLibraryModule extends EOLElement {

    private String name;





    private List<eol_OperationDefinition> eol_operationdefinitions;




    private eol_Import eol_import;




    private List<eol_Import> eol_imports;




    private List<eol_ModelDeclarationStatement> eol_modeldeclarationstatements;


    public eol_EOLLibraryModule(
        String name    ) {
        super(
        );
        this.name = name;
        this.eol_operationdefinitions = new ArrayList<>();
        this.eol_imports = new ArrayList<>();
        this.eol_modeldeclarationstatements = new ArrayList<>();
    }

    public eol_EOLLibraryModule(
        String name        ArrayList<eol_OperationDefinition> eol_operationdefinitions,        ArrayList<eol_Import> eol_imports,        ArrayList<eol_ModelDeclarationStatement> eol_modeldeclarationstatements    ) {
        this.name = name;
        this.eol_operationdefinitions = eol_operationdefinitions;
        this.eol_imports = eol_imports;
        this.eol_modeldeclarationstatements = eol_modeldeclarationstatements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<eol_OperationDefinition> getEol_operationdefinitions() {
        return eol_operationdefinitions;
    }

    public void addEol_operationdefinition(Eol_operationdefinition eol_operationdefinition) {
        this.eol_operationdefinitions.add(eol_operationdefinition);
    }
    public eol_Import getEol_import() {
        return eol_import;
    }

    public void setEol_import(eol_Import eol_import) {
        this.eol_import = eol_import;
    }
    public List<eol_Import> getEol_imports() {
        return eol_imports;
    }

    public void addEol_import(Eol_import eol_import) {
        this.eol_imports.add(eol_import);
    }
    public List<eol_ModelDeclarationStatement> getEol_modeldeclarationstatements() {
        return eol_modeldeclarationstatements;
    }

    public void addEol_modeldeclarationstatement(Eol_modeldeclarationstatement eol_modeldeclarationstatement) {
        this.eol_modeldeclarationstatements.add(eol_modeldeclarationstatement);
    }

}