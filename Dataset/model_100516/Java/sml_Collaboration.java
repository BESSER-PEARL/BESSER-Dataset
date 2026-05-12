





import java.util.List;
import java.util.ArrayList;

public class sml_Collaboration  {

    private String name;





    private sml_Specification sml_specification;




    private List<sml_SmlEPackage> sml_smlepackages;




    private sml_Specification sml_specification;




    private List<sml_Import> sml_imports;


    public sml_Collaboration(
        String name    ) {
        this.name = name;
        this.sml_smlepackages = new ArrayList<>();
        this.sml_imports = new ArrayList<>();
    }

    public sml_Collaboration(
        String name        ArrayList<sml_SmlEPackage> sml_smlepackages,        ArrayList<sml_Import> sml_imports    ) {
        this.name = name;
        this.sml_smlepackages = sml_smlepackages;
        this.sml_imports = sml_imports;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sml_Specification getSml_specification() {
        return sml_specification;
    }

    public void setSml_specification(sml_Specification sml_specification) {
        this.sml_specification = sml_specification;
    }
    public List<sml_SmlEPackage> getSml_smlepackages() {
        return sml_smlepackages;
    }

    public void addSml_smlepackage(Sml_smlepackage sml_smlepackage) {
        this.sml_smlepackages.add(sml_smlepackage);
    }
    public sml_Specification getSml_specification() {
        return sml_specification;
    }

    public void setSml_specification(sml_Specification sml_specification) {
        this.sml_specification = sml_specification;
    }
    public List<sml_Import> getSml_imports() {
        return sml_imports;
    }

    public void addSml_import(Sml_import sml_import) {
        this.sml_imports.add(sml_import);
    }

}