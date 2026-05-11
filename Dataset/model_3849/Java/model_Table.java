





import java.util.List;
import java.util.ArrayList;

public class model_Table  {

    private String name;





    private model_From model_from;


    public model_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_From getModel_from() {
        return model_from;
    }

    public void setModel_from(model_From model_from) {
        this.model_from = model_from;
    }

}