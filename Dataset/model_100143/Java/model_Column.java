





import java.util.List;
import java.util.ArrayList;

public class model_Column extends IColumn {






    private model_Table model_table;




    private model_Type model_type;


    public model_Column(
    ) {
        super(
        );
    }



    public model_Table getModel_table() {
        return model_table;
    }

    public void setModel_table(model_Table model_table) {
        this.model_table = model_table;
    }
    public model_Type getModel_type() {
        return model_type;
    }

    public void setModel_type(model_Type model_type) {
        this.model_type = model_type;
    }

}