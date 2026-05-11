





import java.util.List;
import java.util.ArrayList;

public class Trmodel_Table  {

    private String Name;





    private Trmodel_Operation trmodel_operation;


    public Trmodel_Table(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Trmodel_Operation getTrmodel_operation() {
        return trmodel_operation;
    }

    public void setTrmodel_operation(Trmodel_Operation trmodel_operation) {
        this.trmodel_operation = trmodel_operation;
    }

}