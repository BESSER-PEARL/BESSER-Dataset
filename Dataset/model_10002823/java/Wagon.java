





import java.util.List;
import java.util.ArrayList;

public class Wagon  {

    private None listeDesBandit;
    private None modele;
    private int numeroWagon;
    private String ListedesButin__;





    private List<ModelTraint> modeltraints;


    public Wagon(
        None listeDesBandit,        None modele,        int numeroWagon,        String ListedesButin__    ) {
        this.listeDesBandit = listeDesBandit;
        this.modele = modele;
        this.numeroWagon = numeroWagon;
        this.ListedesButin__ = ListedesButin__;
        this.modeltraints = new ArrayList<>();
    }

    public Wagon(
        None listeDesBandit,        None modele,        int numeroWagon,        String ListedesButin__        ArrayList<ModelTraint> modeltraints    ) {
        this.listeDesBandit = listeDesBandit;
        this.modele = modele;
        this.numeroWagon = numeroWagon;
        this.ListedesButin__ = ListedesButin__;
        this.modeltraints = modeltraints;
    }

    public None getListedesbandit() {
        return listeDesBandit;
    }

    public void setListedesbandit(None listeDesBandit) {
        this.listeDesBandit = listeDesBandit;
    }
    public None getModele() {
        return modele;
    }

    public void setModele(None modele) {
        this.modele = modele;
    }
    public int getNumerowagon() {
        return numeroWagon;
    }

    public void setNumerowagon(int numeroWagon) {
        this.numeroWagon = numeroWagon;
    }
    public String getListedesbutin__() {
        return ListedesButin__;
    }

    public void setListedesbutin__(String ListedesButin__) {
        this.ListedesButin__ = ListedesButin__;
    }

    public List<ModelTraint> getModeltraints() {
        return modeltraints;
    }

    public void addModeltraint(Modeltraint modeltraint) {
        this.modeltraints.add(modeltraint);
    }

}