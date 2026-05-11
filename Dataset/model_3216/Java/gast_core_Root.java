





import java.util.List;
import java.util.ArrayList;

public class gast_core_Root extends ModelElement {

    private int linesOfCode;
    private int linesOfComments;





    private List<BasePath> basepaths;




    private List<StructuralAbstraction> structuralabstractions;




    private List<GASTType> gasttypes;




    private List<Clone> clones;




    private List<Package> packages;


    public gast_core_Root(
        int linesOfCode,        int linesOfComments    ) {
        super(
        );
        this.linesOfCode = linesOfCode;
        this.linesOfComments = linesOfComments;
        this.basepaths = new ArrayList<>();
        this.structuralabstractions = new ArrayList<>();
        this.gasttypes = new ArrayList<>();
        this.clones = new ArrayList<>();
        this.packages = new ArrayList<>();
    }

    public gast_core_Root(
        int linesOfCode,        int linesOfComments        ArrayList<BasePath> basepaths,        ArrayList<StructuralAbstraction> structuralabstractions,        ArrayList<GASTType> gasttypes,        ArrayList<Clone> clones,        ArrayList<Package> packages    ) {
        this.linesOfCode = linesOfCode;
        this.linesOfComments = linesOfComments;
        this.basepaths = basepaths;
        this.structuralabstractions = structuralabstractions;
        this.gasttypes = gasttypes;
        this.clones = clones;
        this.packages = packages;
    }

    public int getLinesofcode() {
        return linesOfCode;
    }

    public void setLinesofcode(int linesOfCode) {
        this.linesOfCode = linesOfCode;
    }
    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
    }

    public List<BasePath> getBasepaths() {
        return basepaths;
    }

    public void addBasepath(Basepath basepath) {
        this.basepaths.add(basepath);
    }
    public List<StructuralAbstraction> getStructuralabstractions() {
        return structuralabstractions;
    }

    public void addStructuralabstraction(Structuralabstraction structuralabstraction) {
        this.structuralabstractions.add(structuralabstraction);
    }
    public List<GASTType> getGasttypes() {
        return gasttypes;
    }

    public void addGasttype(Gasttype gasttype) {
        this.gasttypes.add(gasttype);
    }
    public List<Clone> getClones() {
        return clones;
    }

    public void addClone(Clone clone) {
        this.clones.add(clone);
    }
    public List<Package> getPackages() {
        return packages;
    }

    public void addPackage(Package package) {
        this.packages.add(package);
    }

}