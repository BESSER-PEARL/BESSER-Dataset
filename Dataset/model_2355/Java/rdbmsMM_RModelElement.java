





import java.util.List;
import java.util.ArrayList;

public class rdbmsMM_RModelElement  {

    private String kind;
    private String name;



    public rdbmsMM_RModelElement(
        String kind,        String name    ) {
        this.kind = kind;
        this.name = name;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}