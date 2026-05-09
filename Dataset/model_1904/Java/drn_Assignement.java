





import java.util.List;
import java.util.ArrayList;

public class drn_Assignement  {

    private String name;





    private drn_Model drn_model;




    private drn_Library drn_library;


    public drn_Assignement(
        String name    ) {
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
    public drn_Library getDrn_library() {
        return drn_library;
    }

    public void setDrn_library(drn_Library drn_library) {
        this.drn_library = drn_library;
    }

}