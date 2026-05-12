





import java.util.List;
import java.util.ArrayList;

public class Wagon  {

    private None modele;
    private boolean isInWagon;
    private int numeroWagon;





    private List<ModelTraint> modeltraints;


    public Wagon(
        None modele,        boolean isInWagon,        int numeroWagon    ) {
        this.modele = modele;
        this.isInWagon = isInWagon;
        this.numeroWagon = numeroWagon;
        this.modeltraints = new ArrayList<>();
    }

    public Wagon(
        None modele,        boolean isInWagon,        int numeroWagon        ArrayList<ModelTraint> modeltraints    ) {
        this.modele = modele;
        this.isInWagon = isInWagon;
        this.numeroWagon = numeroWagon;
        this.modeltraints = modeltraints;
    }

    public None getModele() {
        return modele;
    }

    public void setModele(None modele) {
        this.modele = modele;
    }
    public boolean getIsinwagon() {
        return isInWagon;
    }

    public void setIsinwagon(boolean isInWagon) {
        this.isInWagon = isInWagon;
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