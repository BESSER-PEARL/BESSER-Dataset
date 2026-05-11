





import java.util.List;
import java.util.ArrayList;

public class model_Select  {






    private List<model_Column> model_columns;




    private model_Where model_where;




    private model_Union model_union;




    private model_Existence model_existence;




    private model_From model_from;




    private model_Union model_union;


    public model_Select(
    ) {
        this.model_columns = new ArrayList<>();
    }

    public model_Select(
        ArrayList<model_Column> model_columns    ) {
        this.model_columns = model_columns;
    }


    public List<model_Column> getModel_columns() {
        return model_columns;
    }

    public void addModel_column(Model_column model_column) {
        this.model_columns.add(model_column);
    }
    public model_Where getModel_where() {
        return model_where;
    }

    public void setModel_where(model_Where model_where) {
        this.model_where = model_where;
    }
    public model_Union getModel_union() {
        return model_union;
    }

    public void setModel_union(model_Union model_union) {
        this.model_union = model_union;
    }
    public model_Existence getModel_existence() {
        return model_existence;
    }

    public void setModel_existence(model_Existence model_existence) {
        this.model_existence = model_existence;
    }
    public model_From getModel_from() {
        return model_from;
    }

    public void setModel_from(model_From model_from) {
        this.model_from = model_from;
    }
    public model_Union getModel_union() {
        return model_union;
    }

    public void setModel_union(model_Union model_union) {
        this.model_union = model_union;
    }

}