





import java.util.List;
import java.util.ArrayList;

public class abs_Product_reconfiguration  {

    private String name;
    private String update;





    private abs_Product_decl abs_product_decl;




    private List<abs_Delta_id> abs_delta_ids;


    public abs_Product_reconfiguration(
        String name,        String update    ) {
        this.name = name;
        this.update = update;
        this.abs_delta_ids = new ArrayList<>();
    }

    public abs_Product_reconfiguration(
        String name,        String update        ArrayList<abs_Delta_id> abs_delta_ids    ) {
        this.name = name;
        this.update = update;
        this.abs_delta_ids = abs_delta_ids;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUpdate() {
        return update;
    }

    public void setUpdate(String update) {
        this.update = update;
    }

    public abs_Product_decl getAbs_product_decl() {
        return abs_product_decl;
    }

    public void setAbs_product_decl(abs_Product_decl abs_product_decl) {
        this.abs_product_decl = abs_product_decl;
    }
    public List<abs_Delta_id> getAbs_delta_ids() {
        return abs_delta_ids;
    }

    public void addAbs_delta_id(Abs_delta_id abs_delta_id) {
        this.abs_delta_ids.add(abs_delta_id);
    }

}