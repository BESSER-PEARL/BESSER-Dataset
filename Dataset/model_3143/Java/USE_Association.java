





import java.util.List;
import java.util.ArrayList;

public class USE_Association  {

    private String kind;
    private String name;





    private USE_Model use_model;


    public USE_Association(
        String kind,        String name    ) {
        this.kind = kind;
        this.name = name;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public USE_Model getUse_model() {
        return use_model;
    }

    public void setUse_model(USE_Model use_model) {
        this.use_model = use_model;
    }

}