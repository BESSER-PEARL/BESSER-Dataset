





import java.util.List;
import java.util.ArrayList;

public class metamodel_Constraint  {

    private String name;
    private String type;
    private String reference;





    private metamodel_Table metamodel_table;


    public metamodel_Constraint(
        String name,        String type,        String reference    ) {
        this.name = name;
        this.type = type;
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
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }

    public metamodel_Table getMetamodel_table() {
        return metamodel_table;
    }

    public void setMetamodel_table(metamodel_Table metamodel_table) {
        this.metamodel_table = metamodel_table;
    }

}