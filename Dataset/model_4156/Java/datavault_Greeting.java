





import java.util.List;
import java.util.ArrayList;

public class datavault_Greeting  {

    private String name;





    private datavault_Model datavault_model;


    public datavault_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public datavault_Model getDatavault_model() {
        return datavault_model;
    }

    public void setDatavault_model(datavault_Model datavault_model) {
        this.datavault_model = datavault_model;
    }

}