





import java.util.List;
import java.util.ArrayList;

public class gast_core_Package extends NamedModelElement {

    private String qualifiedName;
    private int linesOfComments;
    private int linesOfCode;





    private Package package;




    private List<Package> packages;




    private Root root;




    private List<Package> packages;


    public gast_core_Package(
        String qualifiedName,        int linesOfComments,        int linesOfCode    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
        this.linesOfComments = linesOfComments;
        this.linesOfCode = linesOfCode;
        this.packages = new ArrayList<>();
        this.packages = new ArrayList<>();
    }

    public gast_core_Package(
        String qualifiedName,        int linesOfComments,        int linesOfCode        ArrayList<Package> packages,        ArrayList<Package> packages    ) {
        this.qualifiedName = qualifiedName;
        this.linesOfComments = linesOfComments;
        this.linesOfCode = linesOfCode;
        this.packages = packages;
        this.packages = packages;
    }

    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }
    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
    }
    public int getLinesofcode() {
        return linesOfCode;
    }

    public void setLinesofcode(int linesOfCode) {
        this.linesOfCode = linesOfCode;
    }

    public Package getPackage() {
        return package;
    }

    public void setPackage(Package package) {
        this.package = package;
    }
    public List<Package> getPackages() {
        return packages;
    }

    public void addPackage(Package package) {
        this.packages.add(package);
    }
    public Root getRoot() {
        return root;
    }

    public void setRoot(Root root) {
        this.root = root;
    }
    public List<Package> getPackages() {
        return packages;
    }

    public void addPackage(Package package) {
        this.packages.add(package);
    }

}