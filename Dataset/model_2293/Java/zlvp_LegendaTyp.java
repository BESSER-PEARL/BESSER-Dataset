





import java.util.List;
import java.util.ArrayList;

public class zlvp_LegendaTyp  {

    private int id;
    private String name;





    private zlvp_Legenda zlvp_legenda;


    public zlvp_LegendaTyp(
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

    public zlvp_Legenda getZlvp_legenda() {
        return zlvp_legenda;
    }

    public void setZlvp_legenda(zlvp_Legenda zlvp_legenda) {
        this.zlvp_legenda = zlvp_legenda;
    }

}