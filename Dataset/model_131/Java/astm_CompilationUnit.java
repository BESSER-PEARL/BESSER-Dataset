





import java.util.List;
import java.util.ArrayList;

public class astm_CompilationUnit extends OtherSyntaxObject {

    private String language;



    public astm_CompilationUnit(
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