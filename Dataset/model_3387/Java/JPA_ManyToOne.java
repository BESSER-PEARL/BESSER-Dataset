





import java.util.List;
import java.util.ArrayList;

public class JPA_ManyToOne extends Anotation {

    private String referencedPropertyName;
    private String referencedEntityName;
    private String type;
    private String name;



    public JPA_ManyToOne(
        String referencedPropertyName,        String referencedEntityName,        String type,        String name    ) {
        super(
        );
        this.referencedPropertyName = referencedPropertyName;
        this.referencedEntityName = referencedEntityName;
        this.type = type;
        this.name = name;
    }


    public String getReferencedpropertyname() {
        return referencedPropertyName;
    }

    public void setReferencedpropertyname(String referencedPropertyName) {
        this.referencedPropertyName = referencedPropertyName;
    }
    public String getReferencedentityname() {
        return referencedEntityName;
    }

    public void setReferencedentityname(String referencedEntityName) {
        this.referencedEntityName = referencedEntityName;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}