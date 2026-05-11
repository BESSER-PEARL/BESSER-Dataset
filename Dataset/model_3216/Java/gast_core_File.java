





import java.util.List;
import java.util.ArrayList;

public class gast_core_File extends NamedModelElement {

    private String size;
    private String fullQualifiedPath;
    private int linesOfCode;
    private boolean assemblyFile;
    private boolean sourceFile;
    private String fileSystemPath;





    private List<Package> packages;




    private List<GASTType> gasttypes;




    private List<File> files;




    private List<GASTType> gasttypes;


    public gast_core_File(
        String size,        String fullQualifiedPath,        int linesOfCode,        boolean assemblyFile,        boolean sourceFile,        String fileSystemPath    ) {
        super(
        );
        this.size = size;
        this.fullQualifiedPath = fullQualifiedPath;
        this.linesOfCode = linesOfCode;
        this.assemblyFile = assemblyFile;
        this.sourceFile = sourceFile;
        this.fileSystemPath = fileSystemPath;
        this.packages = new ArrayList<>();
        this.gasttypes = new ArrayList<>();
        this.files = new ArrayList<>();
        this.gasttypes = new ArrayList<>();
    }

    public gast_core_File(
        String size,        String fullQualifiedPath,        int linesOfCode,        boolean assemblyFile,        boolean sourceFile,        String fileSystemPath        ArrayList<Package> packages,        ArrayList<GASTType> gasttypes,        ArrayList<File> files,        ArrayList<GASTType> gasttypes    ) {
        this.size = size;
        this.fullQualifiedPath = fullQualifiedPath;
        this.linesOfCode = linesOfCode;
        this.assemblyFile = assemblyFile;
        this.sourceFile = sourceFile;
        this.fileSystemPath = fileSystemPath;
        this.packages = packages;
        this.gasttypes = gasttypes;
        this.files = files;
        this.gasttypes = gasttypes;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getFullqualifiedpath() {
        return fullQualifiedPath;
    }

    public void setFullqualifiedpath(String fullQualifiedPath) {
        this.fullQualifiedPath = fullQualifiedPath;
    }
    public int getLinesofcode() {
        return linesOfCode;
    }

    public void setLinesofcode(int linesOfCode) {
        this.linesOfCode = linesOfCode;
    }
    public boolean getAssemblyfile() {
        return assemblyFile;
    }

    public void setAssemblyfile(boolean assemblyFile) {
        this.assemblyFile = assemblyFile;
    }
    public boolean getSourcefile() {
        return sourceFile;
    }

    public void setSourcefile(boolean sourceFile) {
        this.sourceFile = sourceFile;
    }
    public String getFilesystempath() {
        return fileSystemPath;
    }

    public void setFilesystempath(String fileSystemPath) {
        this.fileSystemPath = fileSystemPath;
    }

    public List<Package> getPackages() {
        return packages;
    }

    public void addPackage(Package package) {
        this.packages.add(package);
    }
    public List<GASTType> getGasttypes() {
        return gasttypes;
    }

    public void addGasttype(Gasttype gasttype) {
        this.gasttypes.add(gasttype);
    }
    public List<File> getFiles() {
        return files;
    }

    public void addFile(File file) {
        this.files.add(file);
    }
    public List<GASTType> getGasttypes() {
        return gasttypes;
    }

    public void addGasttype(Gasttype gasttype) {
        this.gasttypes.add(gasttype);
    }

}