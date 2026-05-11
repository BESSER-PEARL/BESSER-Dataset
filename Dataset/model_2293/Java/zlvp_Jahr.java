





import java.util.List;
import java.util.ArrayList;

public class zlvp_Jahr  {

    private int id;
    private String name;





    private List<zlvp_Lager> zlvp_lagers;


    public zlvp_Jahr(
        int id,        String name    ) {
        this.id = id;
        this.name = name;
        this.zlvp_lagers = new ArrayList<>();
    }

    public zlvp_Jahr(
        int id,        String name        ArrayList<zlvp_Lager> zlvp_lagers    ) {
        this.id = id;
        this.name = name;
        this.zlvp_lagers = zlvp_lagers;
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

    public List<zlvp_Lager> getZlvp_lagers() {
        return zlvp_lagers;
    }

    public void addZlvp_lager(Zlvp_lager zlvp_lager) {
        this.zlvp_lagers.add(zlvp_lager);
    }

}