





import java.util.List;
import java.util.ArrayList;

public class gast_core_File extends NamedModelElement {

    private boolean sourceFile;
    private int linesOfCode;
    private String fullQualifiedPath;
    private String size;
    private String fileSystemPath;
    private boolean assemblyFile;





    private List<GlobalFunction> globalfunctions;




    private List<GlobalFunction> globalfunctions;




    private Root root;




    private Directory directory;


    public gast_core_File(
        boolean sourceFile,        int linesOfCode,        String fullQualifiedPath,        String size,        String fileSystemPath,        boolean assemblyFile    ) {
        super(
        );
        this.sourceFile = sourceFile;
        this.linesOfCode = linesOfCode;
        this.fullQualifiedPath = fullQualifiedPath;
        this.size = size;
        this.fileSystemPath = fileSystemPath;
        this.assemblyFile = assemblyFile;
        this.globalfunctions = new ArrayList<>();
        this.globalfunctions = new ArrayList<>();
    }

    public gast_core_File(
        boolean sourceFile,        int linesOfCode,        String fullQualifiedPath,        String size,        String fileSystemPath,        boolean assemblyFile        ArrayList<GlobalFunction> globalfunctions,        ArrayList<GlobalFunction> globalfunctions    ) {
        this.sourceFile = sourceFile;
        this.linesOfCode = linesOfCode;
        this.fullQualifiedPath = fullQualifiedPath;
        this.size = size;
        this.fileSystemPath = fileSystemPath;
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
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getFilesystempath() {
        return fileSystemPath;
    }

    public void setFilesystempath(String fileSystemPath) {
        this.fileSystemPath = fileSystemPath;
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