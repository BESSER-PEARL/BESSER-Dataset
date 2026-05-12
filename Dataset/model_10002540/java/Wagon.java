





import java.util.List;
import java.util.ArrayList;

public class Wagon  {

    private String ListedesButin__;
    private None modele;
    private None listeDesBandit;
    private int numeroWagon;





    private List<ModelTraint> modeltraints;


    public Wagon(
        String ListedesButin__,        None modele,        None listeDesBandit,        int numeroWagon    ) {
        this.ListedesButin__ = ListedesButin__;
        this.modele = modele;
        this.listeDesBandit = listeDesBandit;
        this.numeroWagon = numeroWagon;
        this.modeltraints = new ArrayList<>();
    }

    public Wagon(
        String ListedesButin__,        None modele,        None listeDesBandit,        int numeroWagon        ArrayList<ModelTraint> modeltraints    ) {
        this.ListedesButin__ = ListedesButin__;
        this.modele = modele;
        this.listeDesBandit = listeDesBandit;
        this.numeroWagon = numeroWagon;
        this.modeltraints = modeltraints;
    }

    public String getListedesbutin__() {
        return ListedesButin__;
    }

    public void setListedesbutin__(String ListedesButin__) {
        this.ListedesButin__ = ListedesButin__;
    }
    public None getModele() {
        return modele;
    }

    public void setModele(None modele) {
        this.modele = modele;
    }
    public None getListedesbandit() {
        return listeDesBandit;
    }

    public void setListedesbandit(None listeDesBandit) {
        this.listeDesBandit = listeDesBandit;
    }
    public int getNumerowagon() {
        return numeroWagon;
    }

    public void setNumerowagon(int numeroWagon) {
        this.numeroWagon = numeroWagon;
    }

    public List<ModelTraint> getModeltraints() {
        return modeltraints;
    }

    public void addModeltraint(Modeltraint modeltraint) {
        this.modeltraints.add(modeltraint);
    }

}