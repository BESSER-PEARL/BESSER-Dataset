





import java.util.List;
import java.util.ArrayList;

public class Relational_Column  {

    private String name;
    private String id;





    private Relational_Table relational_table;




    private Relational_Table relational_table;


    public Relational_Column(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(Relational_Table relational_table) {
        this.relational_table = relational_table;
    }
    public Relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(Relational_Table relational_table) {
        this.relational_table = relational_table;
    }

}