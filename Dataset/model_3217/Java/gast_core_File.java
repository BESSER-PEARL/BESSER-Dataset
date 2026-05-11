





import java.util.List;
import java.util.ArrayList;

public class gast_core_File extends NamedModelElement {

    private String size;
    private int linesOfCode;
    private String fileSystemPath;
    private String fullQualifiedPath;
    private boolean assemblyFile;
    private boolean sourceFile;





    private Root root;




    private Directory directory;


    public gast_core_File(
        String size,        int linesOfCode,        String fileSystemPath,        String fullQualifiedPath,        boolean assemblyFile,        boolean sourceFile    ) {
        super(
        );
        this.size = size;
        this.linesOfCode = linesOfCode;
        this.fileSystemPath = fileSystemPath;
        this.fullQualifiedPath = fullQualifiedPath;
        this.assemblyFile = assemblyFile;
        this.sourceFile = sourceFile;
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
    public String getFilesystempath() {
        return fileSystemPath;
    }

    public void setFilesystempath(String fileSystemPath) {
        this.fileSystemPath = fileSystemPath;
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
    public boolean getSourcefile() {
        return sourceFile;
    }

    public void setSourcefile(boolean sourceFile) {
        this.sourceFile = sourceFile;
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