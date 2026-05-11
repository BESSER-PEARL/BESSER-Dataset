





import java.util.List;
import java.util.ArrayList;

public class zlvp_Gruppen  {

    private String spruch;
    private String name;
    private int id;





    private zlvp_Leiter zlvp_leiter;




    private zlvp_Lager zlvp_lager;




    private List<zlvp_Leiter> zlvp_leiters;


    public zlvp_Gruppen(
        String spruch,        String name,        int id    ) {
        this.spruch = spruch;
        this.name = name;
        this.id = id;
        this.zlvp_leiters = new ArrayList<>();
    }

    public zlvp_Gruppen(
        String spruch,        String name,        int id        ArrayList<zlvp_Leiter> zlvp_leiters    ) {
        this.spruch = spruch;
        this.name = name;
        this.id = id;
        this.zlvp_leiters = zlvp_leiters;
    }

    public String getSpruch() {
        return spruch;
    }

    public void setSpruch(String spruch) {
        this.spruch = spruch;
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

    public zlvp_Leiter getZlvp_leiter() {
        return zlvp_leiter;
    }

    public void setZlvp_leiter(zlvp_Leiter zlvp_leiter) {
        this.zlvp_leiter = zlvp_leiter;
    }
    public zlvp_Lager getZlvp_lager() {
        return zlvp_lager;
    }

    public void setZlvp_lager(zlvp_Lager zlvp_lager) {
        this.zlvp_lager = zlvp_lager;
    }
    public List<zlvp_Leiter> getZlvp_leiters() {
        return zlvp_leiters;
    }

    public void addZlvp_leiter(Zlvp_leiter zlvp_leiter) {
        this.zlvp_leiters.add(zlvp_leiter);
    }

}