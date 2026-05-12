





import java.util.List;
import java.util.ArrayList;

public class model_MappingSQL extends Mapping {






    private List<model_Column> model_columns;




    private List<model_Column> model_columns;


    public model_MappingSQL(
    ) {
        super(
        );
        this.model_columns = new ArrayList<>();
        this.model_columns = new ArrayList<>();
    }

    public model_MappingSQL(
        ArrayList<model_Column> model_columns,        ArrayList<model_Column> model_columns    ) {
        this.model_columns = model_columns;
        this.model_columns = model_columns;
    }


    public List<model_Column> getModel_columns() {
        return model_columns;
    }

    public void addModel_column(Model_column model_column) {
        this.model_columns.add(model_column);
    }
    public List<model_Column> getModel_columns() {
        return model_columns;
    }

    public void addModel_column(Model_column model_column) {
        this.model_columns.add(model_column);
    }

}