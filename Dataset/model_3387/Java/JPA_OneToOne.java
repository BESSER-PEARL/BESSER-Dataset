





import java.util.List;
import java.util.ArrayList;

public class JPA_OneToOne extends Anotation {

    private String referencedEntityName;
    private String referencedPropertyName;
    private String name;
    private String type;



    public JPA_OneToOne(
        String referencedEntityName,        String referencedPropertyName,        String name,        String type    ) {
        super(
        );
        this.referencedEntityName = referencedEntityName;
        this.referencedPropertyName = referencedPropertyName;
        this.name = name;
        this.type = type;
    }


    public String getReferencedentityname() {
        return referencedEntityName;
    }

    public void setReferencedentityname(String referencedEntityName) {
        this.referencedEntityName = referencedEntityName;
    }
    public String getReferencedpropertyname() {
        return referencedPropertyName;
    }

    public void setReferencedpropertyname(String referencedPropertyName) {
        this.referencedPropertyName = referencedPropertyName;
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