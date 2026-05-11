





import java.util.List;
import java.util.ArrayList;

public class zlvp_Funktion  {

    private int id;
    private String name;





    private zlvp_Stab zlvp_stab;


    public zlvp_Funktion(
        int id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public zlvp_Stab getZlvp_stab() {
        return zlvp_stab;
    }

    public void setZlvp_stab(zlvp_Stab zlvp_stab) {
        this.zlvp_stab = zlvp_stab;
    }

}