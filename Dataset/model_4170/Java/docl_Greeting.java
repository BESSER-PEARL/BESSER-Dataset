





import java.util.List;
import java.util.ArrayList;

public class docl_Greeting  {

    private String name;





    private docl_Model docl_model;


    public docl_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public docl_Model getDocl_model() {
        return docl_model;
    }

    public void setDocl_model(docl_Model docl_model) {
        this.docl_model = docl_model;
    }

}