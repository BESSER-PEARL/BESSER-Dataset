





import java.util.List;
import java.util.ArrayList;

public class workflow_CompilationUnit  {

    private String language;
    private String name;



    public workflow_CompilationUnit(
        String language,        String name    ) {
        this.language = language;
        this.name = name;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}