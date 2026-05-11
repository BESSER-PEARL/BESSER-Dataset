





import java.util.List;
import java.util.ArrayList;

public class urml_Capsule  {

    private boolean root;
    private String name;





    private urml_Model urml_model;


    public urml_Capsule(
        boolean root,        String name    ) {
        this.root = root;
        this.name = name;
    }


    public boolean getRoot() {
        return root;
    }

    public void setRoot(boolean root) {
        this.root = root;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public urml_Model getUrml_model() {
        return urml_model;
    }

    public void setUrml_model(urml_Model urml_model) {
        this.urml_model = urml_model;
    }

}