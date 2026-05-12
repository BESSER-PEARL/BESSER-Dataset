





import java.util.List;
import java.util.ArrayList;

public class useCases_PackageDeclaration  {

    private String name;
    private String description;





    private List<useCases_NamespaceImport> usecases_namespaceimports;




    private useCases_NamespaceImport usecases_namespaceimport;




    private useCases_NamespaceImport usecases_namespaceimport;




    private useCases_NamespaceImport usecases_namespaceimport;




    private useCases_UseCasesModel usecases_usecasesmodel;


    public useCases_PackageDeclaration(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
        this.usecases_namespaceimports = new ArrayList<>();
    }

    public useCases_PackageDeclaration(
        String name,        String description        ArrayList<useCases_NamespaceImport> usecases_namespaceimports    ) {
        this.name = name;
        this.description = description;
        this.usecases_namespaceimports = usecases_namespaceimports;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<useCases_NamespaceImport> getUsecases_namespaceimports() {
        return usecases_namespaceimports;
    }

    public void addUsecases_namespaceimport(Usecases_namespaceimport usecases_namespaceimport) {
        this.usecases_namespaceimports.add(usecases_namespaceimport);
    }
    public useCases_NamespaceImport getUsecases_namespaceimport() {
        return usecases_namespaceimport;
    }

    public void setUsecases_namespaceimport(useCases_NamespaceImport usecases_namespaceimport) {
        this.usecases_namespaceimport = usecases_namespaceimport;
    }
    public useCases_NamespaceImport getUsecases_namespaceimport() {
        return usecases_namespaceimport;
    }

    public void setUsecases_namespaceimport(useCases_NamespaceImport usecases_namespaceimport) {
        this.usecases_namespaceimport = usecases_namespaceimport;
    }
    public useCases_NamespaceImport getUsecases_namespaceimport() {
        return usecases_namespaceimport;
    }

    public void setUsecases_namespaceimport(useCases_NamespaceImport usecases_namespaceimport) {
        this.usecases_namespaceimport = usecases_namespaceimport;
    }
    public useCases_UseCasesModel getUsecases_usecasesmodel() {
        return usecases_usecasesmodel;
    }

    public void setUsecases_usecasesmodel(useCases_UseCasesModel usecases_usecasesmodel) {
        this.usecases_usecasesmodel = usecases_usecasesmodel;
    }

}