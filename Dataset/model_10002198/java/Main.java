





import java.util.List;
import java.util.ArrayList;

public class Main  {

    private String cartes;
    private String bet;
    private int value;





    private List<Carte> cartes;




    private Croupier croupier;


    public Main(
        String cartes,        String bet,        int value    ) {
        this.cartes = cartes;
        this.bet = bet;
        this.value = value;
        this.cartes = new ArrayList<>();
    }

    public Main(
        String cartes,        String bet,        int value        ArrayList<Carte> cartes    ) {
        this.cartes = cartes;
        this.bet = bet;
        this.value = value;
        this.cartes = cartes;
    }

    public String getCartes() {
        return cartes;
    }

    public void setCartes(String cartes) {
        this.cartes = cartes;
    }
    public String getBet() {
        return bet;
    }

    public void setBet(String bet) {
        this.bet = bet;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public List<Carte> getCartes() {
        return cartes;
    }

    public void addCarte(Carte carte) {
        this.cartes.add(carte);
    }
    public Croupier getCroupier() {
        return croupier;
    }

    public void setCroupier(Croupier croupier) {
        this.croupier = croupier;
    }

}