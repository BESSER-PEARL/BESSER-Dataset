





import java.util.List;
import java.util.ArrayList;

public class model_MappingImport extends Mapping {






    private List<model_IColumn> model_icolumns;




    private model_Column model_column;


    public model_MappingImport(
    ) {
        super(
        );
        this.model_icolumns = new ArrayList<>();
    }

    public model_MappingImport(
        ArrayList<model_IColumn> model_icolumns    ) {
        this.model_icolumns = model_icolumns;
    }


    public List<model_IColumn> getModel_icolumns() {
        return model_icolumns;
    }

    public void addModel_icolumn(Model_icolumn model_icolumn) {
        this.model_icolumns.add(model_icolumn);
    }
    public model_Column getModel_column() {
        return model_column;
    }

    public void setModel_column(model_Column model_column) {
        this.model_column = model_column;
    }

}