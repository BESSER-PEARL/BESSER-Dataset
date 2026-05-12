





import java.util.List;
import java.util.ArrayList;

public class Kunde  {

    private String Anschrift;
    private String Name;





    private List<Entlehnung> entlehnungs;


    public Kunde(
        String Anschrift,        String Name    ) {
        this.Anschrift = Anschrift;
        this.Name = Name;
        this.entlehnungs = new ArrayList<>();
    }

    public Kunde(
        String Anschrift,        String Name        ArrayList<Entlehnung> entlehnungs    ) {
        this.Anschrift = Anschrift;
        this.Name = Name;
        this.entlehnungs = entlehnungs;
    }

    public String getAnschrift() {
        return Anschrift;
    }

    public void setAnschrift(String Anschrift) {
        this.Anschrift = Anschrift;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<Entlehnung> getEntlehnungs() {
        return entlehnungs;
    }

    public void addEntlehnung(Entlehnung entlehnung) {
        this.entlehnungs.add(entlehnung);
    }

}