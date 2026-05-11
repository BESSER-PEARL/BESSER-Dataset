





import java.util.List;
import java.util.ArrayList;

public class JPA_OneToMany extends Anotation {

    private String name;
    private String type;
    private String referencedEntityName;



    public JPA_OneToMany(
        String name,        String type,        String referencedEntityName    ) {
        super(
        );
        this.name = name;
        this.type = type;
        this.referencedEntityName = referencedEntityName;
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
    public String getReferencedentityname() {
        return referencedEntityName;
    }

    public void setReferencedentityname(String referencedEntityName) {
        this.referencedEntityName = referencedEntityName;
    }


}