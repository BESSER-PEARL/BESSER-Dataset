





import java.util.List;
import java.util.ArrayList;

public class ACG_Attribute extends ACGElement {

    private String context;
    private String name;



    public ACG_Attribute(
        String context,        String name    ) {
        super(
        );
        this.context = context;
        this.name = name;
    }


    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}