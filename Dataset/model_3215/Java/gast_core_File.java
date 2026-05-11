





import java.util.List;
import java.util.ArrayList;

public class gast_core_File extends NamedModelElement {

    private boolean assemblyFile;
    private String fullQualifiedPath;
    private int linesOfCode;
    private boolean sourceFile;
    private String size;
    private String fileSystemPath;



    public gast_core_File(
        boolean assemblyFile,        String fullQualifiedPath,        int linesOfCode,        boolean sourceFile,        String size,        String fileSystemPath    ) {
        super(
        );
        this.assemblyFile = assemblyFile;
        this.fullQualifiedPath = fullQualifiedPath;
        this.linesOfCode = linesOfCode;
        this.sourceFile = sourceFile;
        this.size = size;
        this.fileSystemPath = fileSystemPath;
    }


    public boolean getAssemblyfile() {
        return assemblyFile;
    }

    public void setAssemblyfile(boolean assemblyFile) {
        this.assemblyFile = assemblyFile;
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
    public boolean getSourcefile() {
        return sourceFile;
    }

    public void setSourcefile(boolean sourceFile) {
        this.sourceFile = sourceFile;
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


}