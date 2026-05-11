





import java.util.List;
import java.util.ArrayList;

public class model_ColumnAlias  {

    private String name;





    private model_Column model_column;


    public model_ColumnAlias(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Column getModel_column() {
        return model_column;
    }

    public void setModel_column(model_Column model_column) {
        this.model_column = model_column;
    }

}