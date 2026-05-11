





import java.util.List;
import java.util.ArrayList;

public class model_Part  {

    private String name;





    private model_Type model_type;


    public model_Part(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Type getModel_type() {
        return model_type;
    }

    public void setModel_type(model_Type model_type) {
        this.model_type = model_type;
    }

}