





import java.util.List;
import java.util.ArrayList;

public class diva_NamedElement extends DiVAModelElement {

    private String name;
    private String id;



    public diva_NamedElement(
        String name,        String id    ) {
        super(
        );
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}