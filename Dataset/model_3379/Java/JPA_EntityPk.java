





import java.util.List;
import java.util.ArrayList;

public class JPA_EntityPk extends Anotation {

    private String name;





    private List<JPA_Property> jpa_propertys;


    public JPA_EntityPk(
        String name    ) {
        super(
        );
        this.name = name;
        this.jpa_propertys = new ArrayList<>();
    }

    public JPA_EntityPk(
        String name        ArrayList<JPA_Property> jpa_propertys    ) {
        this.name = name;
        this.jpa_propertys = jpa_propertys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<JPA_Property> getJpa_propertys() {
        return jpa_propertys;
    }

    public void addJpa_property(Jpa_property jpa_property) {
        this.jpa_propertys.add(jpa_property);
    }

}