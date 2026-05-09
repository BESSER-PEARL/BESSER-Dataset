





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Package extends Namespace, PackageableElement {

    private String URI;





    private CompleteDSLPckg_Package completedslpckg_package;




    private CompleteDSLPckg_Package completedslpckg_package;




    private CompleteDSLPckg_PackageMerge completedslpckg_packagemerge;




    private List<CompleteDSLPckg_PackageMerge> completedslpckg_packagemerges;




    private CompleteDSLPckg_PackageMerge completedslpckg_packagemerge;




    private List<CompleteDSLPckg_PackageableElement> completedslpckg_packageableelements;




    private CompleteDSLPckg_PackageImport completedslpckg_packageimport;


    public CompleteDSLPckg_Package(
        String URI    ) {
        super(
        );
        this.URI = URI;
        this.completedslpckg_packagemerges = new ArrayList<>();
        this.completedslpckg_packageableelements = new ArrayList<>();
    }

    public CompleteDSLPckg_Package(
        String URI        ArrayList<CompleteDSLPckg_PackageMerge> completedslpckg_packagemerges,        ArrayList<CompleteDSLPckg_PackageableElement> completedslpckg_packageableelements    ) {
        this.URI = URI;
        this.completedslpckg_packagemerges = completedslpckg_packagemerges;
        this.completedslpckg_packageableelements = completedslpckg_packageableelements;
    }

    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }

    public CompleteDSLPckg_Package getCompletedslpckg_package() {
        return completedslpckg_package;
    }

    public void setCompletedslpckg_package(CompleteDSLPckg_Package completedslpckg_package) {
        this.completedslpckg_package = completedslpckg_package;
    }
    public CompleteDSLPckg_Package getCompletedslpckg_package() {
        return completedslpckg_package;
    }

    public void setCompletedslpckg_package(CompleteDSLPckg_Package completedslpckg_package) {
        this.completedslpckg_package = completedslpckg_package;
    }
    public CompleteDSLPckg_PackageMerge getCompletedslpckg_packagemerge() {
        return completedslpckg_packagemerge;
    }

    public void setCompletedslpckg_packagemerge(CompleteDSLPckg_PackageMerge completedslpckg_packagemerge) {
        this.completedslpckg_packagemerge = completedslpckg_packagemerge;
    }
    public List<CompleteDSLPckg_PackageMerge> getCompletedslpckg_packagemerges() {
        return completedslpckg_packagemerges;
    }

    public void addCompletedslpckg_packagemerge(Completedslpckg_packagemerge completedslpckg_packagemerge) {
        this.completedslpckg_packagemerges.add(completedslpckg_packagemerge);
    }
    public CompleteDSLPckg_PackageMerge getCompletedslpckg_packagemerge() {
        return completedslpckg_packagemerge;
    }

    public void setCompletedslpckg_packagemerge(CompleteDSLPckg_PackageMerge completedslpckg_packagemerge) {
        this.completedslpckg_packagemerge = completedslpckg_packagemerge;
    }
    public List<CompleteDSLPckg_PackageableElement> getCompletedslpckg_packageableelements() {
        return completedslpckg_packageableelements;
    }

    public void addCompletedslpckg_packageableelement(Completedslpckg_packageableelement completedslpckg_packageableelement) {
        this.completedslpckg_packageableelements.add(completedslpckg_packageableelement);
    }
    public CompleteDSLPckg_PackageImport getCompletedslpckg_packageimport() {
        return completedslpckg_packageimport;
    }

    public void setCompletedslpckg_packageimport(CompleteDSLPckg_PackageImport completedslpckg_packageimport) {
        this.completedslpckg_packageimport = completedslpckg_packageimport;
    }

}