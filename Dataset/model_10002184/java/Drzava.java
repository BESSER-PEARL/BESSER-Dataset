





import java.util.List;
import java.util.ArrayList;

public class Drzava  {

    private int DrzavaID;
    private String NazivDrzave;





    private List<Grad> grads;


    public Drzava(
        int DrzavaID,        String NazivDrzave    ) {
        this.DrzavaID = DrzavaID;
        this.NazivDrzave = NazivDrzave;
        this.grads = new ArrayList<>();
    }

    public Drzava(
        int DrzavaID,        String NazivDrzave        ArrayList<Grad> grads    ) {
        this.DrzavaID = DrzavaID;
        this.NazivDrzave = NazivDrzave;
        this.grads = grads;
    }

    public int getDrzavaid() {
        return DrzavaID;
    }

    public void setDrzavaid(int DrzavaID) {
        this.DrzavaID = DrzavaID;
    }
    public String getNazivdrzave() {
        return NazivDrzave;
    }

    public void setNazivdrzave(String NazivDrzave) {
        this.NazivDrzave = NazivDrzave;
    }

    public List<Grad> getGrads() {
        return grads;
    }

    public void addGrad(Grad grad) {
        this.grads.add(grad);
    }

}