





import java.util.List;
import java.util.ArrayList;

public class rell_Operation  {

    private String name;





    private rell_Model rell_model;


    public rell_Operation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rell_Model getRell_model() {
        return rell_model;
    }

    public void setRell_model(rell_Model rell_model) {
        this.rell_model = rell_model;
    }

}