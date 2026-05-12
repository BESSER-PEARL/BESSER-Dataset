





import java.util.List;
import java.util.ArrayList;

public class Relational_Constraint  {

    private String name;
    private String description;





    private Relational_Domain relational_domain;


    public Relational_Constraint(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Relational_Domain getRelational_domain() {
        return relational_domain;
    }

    public void setRelational_domain(Relational_Domain relational_domain) {
        this.relational_domain = relational_domain;
    }

}