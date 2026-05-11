





import java.util.List;
import java.util.ArrayList;

public class JPA_Entity  {

    private String comment;
    private String name;





    private JPA_PersistenceUnit jpa_persistenceunit;


    public JPA_Entity(
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

    public JPA_PersistenceUnit getJpa_persistenceunit() {
        return jpa_persistenceunit;
    }

    public void setJpa_persistenceunit(JPA_PersistenceUnit jpa_persistenceunit) {
        this.jpa_persistenceunit = jpa_persistenceunit;
    }

}