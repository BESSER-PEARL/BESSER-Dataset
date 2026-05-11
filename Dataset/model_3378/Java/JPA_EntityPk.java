





import java.util.List;
import java.util.ArrayList;

public class JPA_EntityPk extends Anotation {

    private String name;



    public JPA_EntityPk(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}