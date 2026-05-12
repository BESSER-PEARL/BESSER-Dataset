





import java.util.List;
import java.util.ArrayList;

public class model_MappingExport extends Mapping {






    private List<model_Column> model_columns;




    private model_IColumn model_icolumn;


    public model_MappingExport(
    ) {
        super(
        );
        this.model_columns = new ArrayList<>();
    }

    public model_MappingExport(
        ArrayList<model_Column> model_columns    ) {
        this.model_columns = model_columns;
    }


    public List<model_Column> getModel_columns() {
        return model_columns;
    }

    public void addModel_column(Model_column model_column) {
        this.model_columns.add(model_column);
    }
    public model_IColumn getModel_icolumn() {
        return model_icolumn;
    }

    public void setModel_icolumn(model_IColumn model_icolumn) {
        this.model_icolumn = model_icolumn;
    }

}