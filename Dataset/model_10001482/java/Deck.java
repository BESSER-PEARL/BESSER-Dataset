





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String sektion;
    private boolean fahrtWunsch;





    private List<Kabine> kabines;




    private List<Kabine> kabines;




    private List<TurboliftSchacht> turboliftschachts;


    public Deck(
        String sektion,        boolean fahrtWunsch    ) {
        this.sektion = sektion;
        this.fahrtWunsch = fahrtWunsch;
        this.kabines = new ArrayList<>();
        this.kabines = new ArrayList<>();
        this.turboliftschachts = new ArrayList<>();
    }

    public Deck(
        String sektion,        boolean fahrtWunsch        ArrayList<Kabine> kabines,        ArrayList<Kabine> kabines,        ArrayList<TurboliftSchacht> turboliftschachts    ) {
        this.sektion = sektion;
        this.fahrtWunsch = fahrtWunsch;
        this.kabines = kabines;
        this.kabines = kabines;
        this.turboliftschachts = turboliftschachts;
    }

    public String getSektion() {
        return sektion;
    }

    public void setSektion(String sektion) {
        this.sektion = sektion;
    }
    public boolean getFahrtwunsch() {
        return fahrtWunsch;
    }

    public void setFahrtwunsch(boolean fahrtWunsch) {
        this.fahrtWunsch = fahrtWunsch;
    }

    public List<Kabine> getKabines() {
        return kabines;
    }

    public void addKabine(Kabine kabine) {
        this.kabines.add(kabine);
    }
    public List<Kabine> getKabines() {
        return kabines;
    }

    public void addKabine(Kabine kabine) {
        this.kabines.add(kabine);
    }
    public List<TurboliftSchacht> getTurboliftschachts() {
        return turboliftschachts;
    }

    public void addTurboliftschacht(Turboliftschacht turboliftschacht) {
        this.turboliftschachts.add(turboliftschacht);
    }

}