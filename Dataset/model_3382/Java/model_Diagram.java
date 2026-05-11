





import java.util.List;
import java.util.ArrayList;

public class model_Diagram  {






    private List<model_Table> model_tables;


    public model_Diagram(
    ) {
        this.model_tables = new ArrayList<>();
    }

    public model_Diagram(
        ArrayList<model_Table> model_tables    ) {
        this.model_tables = model_tables;
    }


    public List<model_Table> getModel_tables() {
        return model_tables;
    }

    public void addModel_table(Model_table model_table) {
        this.model_tables.add(model_table);
    }

}