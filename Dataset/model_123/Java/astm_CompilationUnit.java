





import java.util.List;
import java.util.ArrayList;

public class astm_CompilationUnit extends OtherSyntaxObject {

    private String language;





    private astm_Project astm_project;


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

    public astm_Project getAstm_project() {
        return astm_project;
    }

    public void setAstm_project(astm_Project astm_project) {
        this.astm_project = astm_project;
    }

}