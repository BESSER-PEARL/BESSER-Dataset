





import java.util.List;
import java.util.ArrayList;

public class JPA_Property  {

    private String name;
    private String comment;





    private JPA_Entity jpa_entity;




    private JPA_EntityPk jpa_entitypk;


    public JPA_Property(
        String name,        String comment    ) {
        this.name = name;
        this.comment = comment;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public JPA_Entity getJpa_entity() {
        return jpa_entity;
    }

    public void setJpa_entity(JPA_Entity jpa_entity) {
        this.jpa_entity = jpa_entity;
    }
    public JPA_EntityPk getJpa_entitypk() {
        return jpa_entitypk;
    }

    public void setJpa_entitypk(JPA_EntityPk jpa_entitypk) {
        this.jpa_entitypk = jpa_entitypk;
    }

}