





import java.util.List;
import java.util.ArrayList;

public class conference_Site  {

    private String documentation;
    private String name;



    public conference_Site(
        String documentation,        String name    ) {
        this.documentation = documentation;
        this.name = name;
    }


    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}