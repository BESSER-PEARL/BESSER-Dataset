





import java.util.List;
import java.util.ArrayList;

public class zlvp_Teilnehmer  {

    private int id;





    private zlvp_Person zlvp_person;




    private zlvp_Gruppen zlvp_gruppen;




    private List<zlvp_Gruppen> zlvp_gruppens;


    public zlvp_Teilnehmer(
        int id    ) {
        this.id = id;
        this.zlvp_gruppens = new ArrayList<>();
    }

    public zlvp_Teilnehmer(
        int id        ArrayList<zlvp_Gruppen> zlvp_gruppens    ) {
        this.id = id;
        this.zlvp_gruppens = zlvp_gruppens;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public zlvp_Person getZlvp_person() {
        return zlvp_person;
    }

    public void setZlvp_person(zlvp_Person zlvp_person) {
        this.zlvp_person = zlvp_person;
    }
    public zlvp_Gruppen getZlvp_gruppen() {
        return zlvp_gruppen;
    }

    public void setZlvp_gruppen(zlvp_Gruppen zlvp_gruppen) {
        this.zlvp_gruppen = zlvp_gruppen;
    }
    public List<zlvp_Gruppen> getZlvp_gruppens() {
        return zlvp_gruppens;
    }

    public void addZlvp_gruppen(Zlvp_gruppen zlvp_gruppen) {
        this.zlvp_gruppens.add(zlvp_gruppen);
    }

}