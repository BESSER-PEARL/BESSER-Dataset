





import java.util.List;
import java.util.ArrayList;

public class workflow_CompilationUnit  {

    private String name;
    private String language;



    public workflow_CompilationUnit(
        String name,        String language    ) {
        this.name = name;
        this.language = language;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }


}