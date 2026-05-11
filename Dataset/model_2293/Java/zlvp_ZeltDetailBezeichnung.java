





import java.util.List;
import java.util.ArrayList;

public class zlvp_ZeltDetailBezeichnung  {

    private String name;
    private int id;





    private zlvp_ZeltDetail zlvp_zeltdetail;


    public zlvp_ZeltDetailBezeichnung(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public zlvp_ZeltDetail getZlvp_zeltdetail() {
        return zlvp_zeltdetail;
    }

    public void setZlvp_zeltdetail(zlvp_ZeltDetail zlvp_zeltdetail) {
        this.zlvp_zeltdetail = zlvp_zeltdetail;
    }

}