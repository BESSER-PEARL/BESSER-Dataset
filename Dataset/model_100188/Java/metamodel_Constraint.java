





import java.util.List;
import java.util.ArrayList;

public class metamodel_Constraint  {

    private String reference;
    private String name;
    private String type;



    public metamodel_Constraint(
        String reference,        String name,        String type    ) {
        this.reference = reference;
        this.name = name;
        this.type = type;
    }


    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}