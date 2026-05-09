





import java.util.List;
import java.util.ArrayList;

public class java_Archive extends NamedElement {

    private String originalFilePath;



    public java_Archive(
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