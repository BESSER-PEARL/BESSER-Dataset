





import java.util.List;
import java.util.ArrayList;

public class gast_core_File extends NamedModelElement {

    private boolean sourceFile;
    private String fileSystemPath;
    private String size;
    private int linesOfCode;
    private String fullQualifiedPath;
    private boolean assemblyFile;





    private List<GlobalFunction> globalfunctions;




    private List<GlobalFunction> globalfunctions;




    private Root root;




    private Directory directory;


    public gast_core_File(
        boolean sourceFile,        String fileSystemPath,        String size,        int linesOfCode,        String fullQualifiedPath,        boolean assemblyFile    ) {
        super(
        );
        this.sourceFile = sourceFile;
        this.fileSystemPath = fileSystemPath;
        this.size = size;
        this.linesOfCode = linesOfCode;
        this.fullQualifiedPath = fullQualifiedPath;
        this.assemblyFile = assemblyFile;
        this.globalfunctions = new ArrayList<>();
        this.globalfunctions = new ArrayList<>();
    }

    public gast_core_File(
        boolean sourceFile,        String fileSystemPath,        String size,        int linesOfCode,        String fullQualifiedPath,        boolean assemblyFile        ArrayList<GlobalFunction> globalfunctions,        ArrayList<GlobalFunction> globalfunctions    ) {
        this.sourceFile = sourceFile;
        this.fileSystemPath = fileSystemPath;
        this.size = size;
        this.linesOfCode = linesOfCode;
        this.fullQualifiedPath = fullQualifiedPath;
        this.assemblyFile = assemblyFile;
        this.globalfunctions = globalfunctions;
        this.globalfunctions = globalfunctions;
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
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public int getLinesofcode() {
        return linesOfCode;
    }

    public void setLinesofcode(int linesOfCode) {
        this.linesOfCode = linesOfCode;
    }
    public String getFullqualifiedpath() {
        return fullQualifiedPath;
    }

    public void setFullqualifiedpath(String fullQualifiedPath) {
        this.fullQualifiedPath = fullQualifiedPath;
    }
    public boolean getAssemblyfile() {
        return assemblyFile;
    }

    public void setAssemblyfile(boolean assemblyFile) {
        this.assemblyFile = assemblyFile;
    }

    public List<GlobalFunction> getGlobalfunctions() {
        return globalfunctions;
    }

    public void addGlobalfunction(Globalfunction globalfunction) {
        this.globalfunctions.add(globalfunction);
    }
    public List<GlobalFunction> getGlobalfunctions() {
        return globalfunctions;
    }

    public void addGlobalfunction(Globalfunction globalfunction) {
        this.globalfunctions.add(globalfunction);
    }
    public Root getRoot() {
        return root;
    }

    public void setRoot(Root root) {
        this.root = root;
    }
    public Directory getDirectory() {
        return directory;
    }

    public void setDirectory(Directory directory) {
        this.directory = directory;
    }

}