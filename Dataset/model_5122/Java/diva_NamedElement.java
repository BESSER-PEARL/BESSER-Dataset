





import java.util.List;
import java.util.ArrayList;

public class diva_NamedElement extends DiVAModelElement {

    private String id;
    private String name;



    public diva_NamedElement(
        String id,        String name    ) {
        super(
        );
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