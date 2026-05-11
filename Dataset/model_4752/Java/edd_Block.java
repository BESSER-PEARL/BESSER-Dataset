





import java.util.List;
import java.util.ArrayList;

public class edd_Block  {

    private String name;





    private edd_Model edd_model;


    public edd_Block(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public edd_Model getEdd_model() {
        return edd_model;
    }

    public void setEdd_model(edd_Model edd_model) {
        this.edd_model = edd_model;
    }

}