





import java.util.List;
import java.util.ArrayList;

public class gastm_CompilationUnit extends SourceFile {

    private String language;



    public gastm_CompilationUnit(
        String language    ) {
        super(
        );
        this.language = language;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }


}