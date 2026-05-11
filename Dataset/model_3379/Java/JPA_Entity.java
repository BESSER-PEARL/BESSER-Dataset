





import java.util.List;
import java.util.ArrayList;

public class JPA_Entity  {

    private String name;
    private String comment;





    private JPA_PersistenceUnit jpa_persistenceunit;


    public JPA_Entity(
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

    public JPA_PersistenceUnit getJpa_persistenceunit() {
        return jpa_persistenceunit;
    }

    public void setJpa_persistenceunit(JPA_PersistenceUnit jpa_persistenceunit) {
        this.jpa_persistenceunit = jpa_persistenceunit;
    }

}