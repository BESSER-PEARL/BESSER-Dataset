





import java.util.List;
import java.util.ArrayList;

public class UML_14_root  {






    private List<UML_14_Schachtel> uml_14_schachtels;


    public UML_14_root(
    ) {
        this.uml_14_schachtels = new ArrayList<>();
    }

    public UML_14_root(
        ArrayList<UML_14_Schachtel> uml_14_schachtels    ) {
        this.uml_14_schachtels = uml_14_schachtels;
    }


    public List<UML_14_Schachtel> getUml_14_schachtels() {
        return uml_14_schachtels;
    }

    public void addUml_14_schachtel(Uml_14_schachtel uml_14_schachtel) {
        this.uml_14_schachtels.add(uml_14_schachtel);
    }

}