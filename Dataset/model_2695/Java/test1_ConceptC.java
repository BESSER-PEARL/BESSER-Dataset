





import java.util.List;
import java.util.ArrayList;

public class test1_ConceptC  {

    private int nbr;
    private boolean cool;





    private test1_ConceptA test1_concepta;


    public test1_ConceptC(
        int nbr,        boolean cool    ) {
        this.nbr = nbr;
        this.cool = cool;
    }


    public int getNbr() {
        return nbr;
    }

    public void setNbr(int nbr) {
        this.nbr = nbr;
    }
    public boolean getCool() {
        return cool;
    }

    public void setCool(boolean cool) {
        this.cool = cool;
    }

    public test1_ConceptA getTest1_concepta() {
        return test1_concepta;
    }

    public void setTest1_concepta(test1_ConceptA test1_concepta) {
        this.test1_concepta = test1_concepta;
    }

}