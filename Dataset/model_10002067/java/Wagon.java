





import java.util.List;
import java.util.ArrayList;

public class Wagon  {

    private boolean isInWagon;
    private None modele;
    private int numeroWagon;





    private List<ModelTraint> modeltraints;


    public Wagon(
        boolean isInWagon,        None modele,        int numeroWagon    ) {
        this.isInWagon = isInWagon;
        this.modele = modele;
        this.numeroWagon = numeroWagon;
        this.modeltraints = new ArrayList<>();
    }

    public Wagon(
        boolean isInWagon,        None modele,        int numeroWagon        ArrayList<ModelTraint> modeltraints    ) {
        this.isInWagon = isInWagon;
        this.modele = modele;
        this.numeroWagon = numeroWagon;
        this.modeltraints = modeltraints;
    }

    public boolean getIsinwagon() {
        return isInWagon;
    }

    public void setIsinwagon(boolean isInWagon) {
        this.isInWagon = isInWagon;
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

    public List<ModelTraint> getModeltraints() {
        return modeltraints;
    }

    public void addModeltraint(Modeltraint modeltraint) {
        this.modeltraints.add(modeltraint);
    }

}