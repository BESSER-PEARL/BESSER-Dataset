





import java.util.List;
import java.util.ArrayList;

public class umltordbms_PrimitiveToName  {

    private String name;
    private String typeName;



    public umltordbms_PrimitiveToName(
        String name,        String typeName    ) {
        this.name = name;
        this.typeName = typeName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }


}