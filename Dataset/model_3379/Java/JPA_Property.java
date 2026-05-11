





import java.util.List;
import java.util.ArrayList;

public class JPA_Property  {

    private String comment;
    private String name;





    private JPA_Entity jpa_entity;


    public JPA_Property(
        String comment,        String name    ) {
        this.comment = comment;
        this.name = name;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public JPA_Entity getJpa_entity() {
        return jpa_entity;
    }

    public void setJpa_entity(JPA_Entity jpa_entity) {
        this.jpa_entity = jpa_entity;
    }

}