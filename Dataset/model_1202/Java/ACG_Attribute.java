





import java.util.List;
import java.util.ArrayList;

public class ACG_Attribute extends ACGElement {

    private String name;
    private String context;



    public ACG_Attribute(
        String name,        String context    ) {
        super(
        );
        this.name = name;
        this.context = context;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }


}