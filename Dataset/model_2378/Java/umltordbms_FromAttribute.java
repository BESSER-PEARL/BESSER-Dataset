





import java.util.List;
import java.util.ArrayList;

public class umltordbms_FromAttribute  {

    private String name;
    private String kind;



    public umltordbms_FromAttribute(
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