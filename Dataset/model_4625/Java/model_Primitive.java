





import java.util.List;
import java.util.ArrayList;

public class model_Primitive  {

    private String name;





    private model_Symbol model_symbol;


    public model_Primitive(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Symbol getModel_symbol() {
        return model_symbol;
    }

    public void setModel_symbol(model_Symbol model_symbol) {
        this.model_symbol = model_symbol;
    }

}