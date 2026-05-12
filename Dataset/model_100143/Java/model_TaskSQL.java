





import java.util.List;
import java.util.ArrayList;

public class model_TaskSQL extends Task {






    private model_Table model_table;




    private List<model_MappingSQL> model_mappingsqls;




    private model_Table model_table;


    public model_TaskSQL(
    ) {
        super(
        );
        this.model_mappingsqls = new ArrayList<>();
    }

    public model_TaskSQL(
        ArrayList<model_MappingSQL> model_mappingsqls    ) {
        this.model_mappingsqls = model_mappingsqls;
    }


    public model_Table getModel_table() {
        return model_table;
    }

    public void setModel_table(model_Table model_table) {
        this.model_table = model_table;
    }
    public List<model_MappingSQL> getModel_mappingsqls() {
        return model_mappingsqls;
    }

    public void addModel_mappingsql(Model_mappingsql model_mappingsql) {
        this.model_mappingsqls.add(model_mappingsql);
    }
    public model_Table getModel_table() {
        return model_table;
    }

    public void setModel_table(model_Table model_table) {
        this.model_table = model_table;
    }

}