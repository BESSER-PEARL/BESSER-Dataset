





import java.util.List;
import java.util.ArrayList;

public class drn_Context  {

    private String name;
    private String where;





    private drn_Model drn_model;


    public drn_Context(
        String name,        String where    ) {
        this.name = name;
        this.where = where;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWhere() {
        return where;
    }

    public void setWhere(String where) {
        this.where = where;
    }

    public drn_Model getDrn_model() {
        return drn_model;
    }

    public void setDrn_model(drn_Model drn_model) {
        this.drn_model = drn_model;
    }

}