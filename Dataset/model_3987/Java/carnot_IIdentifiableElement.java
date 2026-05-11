





import java.util.List;
import java.util.ArrayList;

public class carnot_IIdentifiableElement  {

    private String id;
    private String name;



    public carnot_IIdentifiableElement(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}