





import java.util.List;
import java.util.ArrayList;

public class simpleuml_UMLModelElement  {

    private String name;
    private String kind;



    public simpleuml_UMLModelElement(
        String name,        String kind    ) {
        this.name = name;
        this.kind = kind;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}