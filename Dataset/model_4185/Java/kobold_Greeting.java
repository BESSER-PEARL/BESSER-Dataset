





import java.util.List;
import java.util.ArrayList;

public class kobold_Greeting  {

    private String name;





    private kobold_Model kobold_model;


    public kobold_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public kobold_Model getKobold_model() {
        return kobold_model;
    }

    public void setKobold_model(kobold_Model kobold_model) {
        this.kobold_model = kobold_model;
    }

}