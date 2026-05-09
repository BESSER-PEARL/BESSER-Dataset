





import java.util.List;
import java.util.ArrayList;

public class java_CompilationUnit extends NamedElement {

    private String originalFilePath;



    public java_CompilationUnit(
        String originalFilePath    ) {
        super(
        );
        this.originalFilePath = originalFilePath;
    }


    public String getOriginalfilepath() {
        return originalFilePath;
    }

    public void setOriginalfilepath(String originalFilePath) {
        this.originalFilePath = originalFilePath;
    }


}