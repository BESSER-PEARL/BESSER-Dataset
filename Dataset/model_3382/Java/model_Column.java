





import java.util.List;
import java.util.ArrayList;

public class model_Column  {

    private String name;





    private model_Table model_table;


    public model_Column(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Table getModel_table() {
        return model_table;
    }

    public void setModel_table(model_Table model_table) {
        this.model_table = model_table;
    }

}