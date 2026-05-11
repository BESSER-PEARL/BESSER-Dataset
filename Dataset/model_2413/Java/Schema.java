





import java.util.List;
import java.util.ArrayList;

public class Schema  {






    private Relational_System relational_system;




    private Relational_Table relational_table;


    public Schema(
    ) {
    }



    public Relational_System getRelational_system() {
        return relational_system;
    }

    public void setRelational_system(Relational_System relational_system) {
        this.relational_system = relational_system;
    }
    public Relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(Relational_Table relational_table) {
        this.relational_table = relational_table;
    }

}