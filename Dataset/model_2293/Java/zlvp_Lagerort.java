





import java.util.List;
import java.util.ArrayList;

public class zlvp_Lagerort  {

    private String name;
    private int id;





    private zlvp_Lager zlvp_lager;




    private List<zlvp_Lager> zlvp_lagers;


    public zlvp_Lagerort(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
        this.zlvp_lagers = new ArrayList<>();
    }

    public zlvp_Lagerort(
        String name,        int id        ArrayList<zlvp_Lager> zlvp_lagers    ) {
        this.name = name;
        this.id = id;
        this.zlvp_lagers = zlvp_lagers;
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

    public zlvp_Lager getZlvp_lager() {
        return zlvp_lager;
    }

    public void setZlvp_lager(zlvp_Lager zlvp_lager) {
        this.zlvp_lager = zlvp_lager;
    }
    public List<zlvp_Lager> getZlvp_lagers() {
        return zlvp_lagers;
    }

    public void addZlvp_lager(Zlvp_lager zlvp_lager) {
        this.zlvp_lagers.add(zlvp_lager);
    }

}