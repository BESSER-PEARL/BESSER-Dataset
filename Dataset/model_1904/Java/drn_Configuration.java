





import java.util.List;
import java.util.ArrayList;

public class drn_Configuration extends Root {

    private String name;





    private drn_Model drn_model;


    public drn_Configuration(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public drn_Model getDrn_model() {
        return drn_model;
    }

    public void setDrn_model(drn_Model drn_model) {
        this.drn_model = drn_model;
    }

}