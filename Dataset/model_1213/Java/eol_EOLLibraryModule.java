





import java.util.List;
import java.util.ArrayList;

public class eol_EOLLibraryModule extends EOLElement {

    private String name;





    private List<eol_OperationDefinition> eol_operationdefinitions;




    private List<eol_IModel> eol_imodels;




    private eol_Import eol_import;




    private List<eol_Import> eol_imports;


    public eol_EOLLibraryModule(
        String name    ) {
        super(
        );
        this.name = name;
        this.eol_operationdefinitions = new ArrayList<>();
        this.eol_imodels = new ArrayList<>();
        this.eol_imports = new ArrayList<>();
    }

    public eol_EOLLibraryModule(
        String name        ArrayList<eol_OperationDefinition> eol_operationdefinitions,        ArrayList<eol_IModel> eol_imodels,        ArrayList<eol_Import> eol_imports    ) {
        this.name = name;
        this.eol_operationdefinitions = eol_operationdefinitions;
        this.eol_imodels = eol_imodels;
        this.eol_imports = eol_imports;
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
    public List<eol_IModel> getEol_imodels() {
        return eol_imodels;
    }

    public void addEol_imodel(Eol_imodel eol_imodel) {
        this.eol_imodels.add(eol_imodel);
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

}