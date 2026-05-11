





import java.util.List;
import java.util.ArrayList;

public class zlvp_Zelt  {

    private String name;
    private int id;





    private List<zlvp_ZeltDetail> zlvp_zeltdetails;




    private List<zlvp_Verleih> zlvp_verleihs;




    private zlvp_Lager zlvp_lager;




    private List<zlvp_Schaeden> zlvp_schaedens;




    private List<zlvp_Lager> zlvp_lagers;


    public zlvp_Zelt(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
        this.zlvp_zeltdetails = new ArrayList<>();
        this.zlvp_verleihs = new ArrayList<>();
        this.zlvp_schaedens = new ArrayList<>();
        this.zlvp_lagers = new ArrayList<>();
    }

    public zlvp_Zelt(
        String name,        int id        ArrayList<zlvp_ZeltDetail> zlvp_zeltdetails,        ArrayList<zlvp_Verleih> zlvp_verleihs,        ArrayList<zlvp_Schaeden> zlvp_schaedens,        ArrayList<zlvp_Lager> zlvp_lagers    ) {
        this.name = name;
        this.id = id;
        this.zlvp_zeltdetails = zlvp_zeltdetails;
        this.zlvp_verleihs = zlvp_verleihs;
        this.zlvp_schaedens = zlvp_schaedens;
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

    public List<zlvp_ZeltDetail> getZlvp_zeltdetails() {
        return zlvp_zeltdetails;
    }

    public void addZlvp_zeltdetail(Zlvp_zeltdetail zlvp_zeltdetail) {
        this.zlvp_zeltdetails.add(zlvp_zeltdetail);
    }
    public List<zlvp_Verleih> getZlvp_verleihs() {
        return zlvp_verleihs;
    }

    public void addZlvp_verleih(Zlvp_verleih zlvp_verleih) {
        this.zlvp_verleihs.add(zlvp_verleih);
    }
    public zlvp_Lager getZlvp_lager() {
        return zlvp_lager;
    }

    public void setZlvp_lager(zlvp_Lager zlvp_lager) {
        this.zlvp_lager = zlvp_lager;
    }
    public List<zlvp_Schaeden> getZlvp_schaedens() {
        return zlvp_schaedens;
    }

    public void addZlvp_schaeden(Zlvp_schaeden zlvp_schaeden) {
        this.zlvp_schaedens.add(zlvp_schaeden);
    }
    public List<zlvp_Lager> getZlvp_lagers() {
        return zlvp_lagers;
    }

    public void addZlvp_lager(Zlvp_lager zlvp_lager) {
        this.zlvp_lagers.add(zlvp_lager);
    }

}