





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlAnnotation  {

    private String type;
    private String contents;



    public sADL_SadlAnnotation(
        String type,        String contents    ) {
        this.type = type;
        this.contents = contents;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getContents() {
        return contents;
    }

    public void setContents(String contents) {
        this.contents = contents;
    }


}