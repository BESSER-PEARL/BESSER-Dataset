





import java.util.List;
import java.util.ArrayList;

public class simpleocl_Module extends NamedElement {






    private List<simpleocl_OclMetamodel> simpleocl_oclmetamodels;




    private simpleocl_Import simpleocl_import;




    private List<simpleocl_Import> simpleocl_imports;




    private simpleocl_ModuleElement simpleocl_moduleelement;




    private List<simpleocl_ModuleElement> simpleocl_moduleelements;


    public simpleocl_Module(
    ) {
        super(
        );
        this.simpleocl_oclmetamodels = new ArrayList<>();
        this.simpleocl_imports = new ArrayList<>();
        this.simpleocl_moduleelements = new ArrayList<>();
    }

    public simpleocl_Module(
        ArrayList<simpleocl_OclMetamodel> simpleocl_oclmetamodels,        ArrayList<simpleocl_Import> simpleocl_imports,        ArrayList<simpleocl_ModuleElement> simpleocl_moduleelements    ) {
        this.simpleocl_oclmetamodels = simpleocl_oclmetamodels;
        this.simpleocl_imports = simpleocl_imports;
        this.simpleocl_moduleelements = simpleocl_moduleelements;
    }


    public List<simpleocl_OclMetamodel> getSimpleocl_oclmetamodels() {
        return simpleocl_oclmetamodels;
    }

    public void addSimpleocl_oclmetamodel(Simpleocl_oclmetamodel simpleocl_oclmetamodel) {
        this.simpleocl_oclmetamodels.add(simpleocl_oclmetamodel);
    }
    public simpleocl_Import getSimpleocl_import() {
        return simpleocl_import;
    }

    public void setSimpleocl_import(simpleocl_Import simpleocl_import) {
        this.simpleocl_import = simpleocl_import;
    }
    public List<simpleocl_Import> getSimpleocl_imports() {
        return simpleocl_imports;
    }

    public void addSimpleocl_import(Simpleocl_import simpleocl_import) {
        this.simpleocl_imports.add(simpleocl_import);
    }
    public simpleocl_ModuleElement getSimpleocl_moduleelement() {
        return simpleocl_moduleelement;
    }

    public void setSimpleocl_moduleelement(simpleocl_ModuleElement simpleocl_moduleelement) {
        this.simpleocl_moduleelement = simpleocl_moduleelement;
    }
    public List<simpleocl_ModuleElement> getSimpleocl_moduleelements() {
        return simpleocl_moduleelements;
    }

    public void addSimpleocl_moduleelement(Simpleocl_moduleelement simpleocl_moduleelement) {
        this.simpleocl_moduleelements.add(simpleocl_moduleelement);
    }

}