





import java.util.List;
import java.util.ArrayList;

public class UML_14_Konzept extends Benanntes {

    private String istAktiev;





    private UML_14_Schachtel uml_14_schachtel;




    private List<UML_14_Eigenschaft> uml_14_eigenschafts;




    private List<UML_14_Verhalten> uml_14_verhaltens;


    public UML_14_Konzept(
        String istAktiev    ) {
        super(
        );
        this.istAktiev = istAktiev;
        this.uml_14_eigenschafts = new ArrayList<>();
        this.uml_14_verhaltens = new ArrayList<>();
    }

    public UML_14_Konzept(
        String istAktiev        ArrayList<UML_14_Eigenschaft> uml_14_eigenschafts,        ArrayList<UML_14_Verhalten> uml_14_verhaltens    ) {
        this.istAktiev = istAktiev;
        this.uml_14_eigenschafts = uml_14_eigenschafts;
        this.uml_14_verhaltens = uml_14_verhaltens;
    }

    public String getIstaktiev() {
        return istAktiev;
    }

    public void setIstaktiev(String istAktiev) {
        this.istAktiev = istAktiev;
    }

    public UML_14_Schachtel getUml_14_schachtel() {
        return uml_14_schachtel;
    }

    public void setUml_14_schachtel(UML_14_Schachtel uml_14_schachtel) {
        this.uml_14_schachtel = uml_14_schachtel;
    }
    public List<UML_14_Eigenschaft> getUml_14_eigenschafts() {
        return uml_14_eigenschafts;
    }

    public void addUml_14_eigenschaft(Uml_14_eigenschaft uml_14_eigenschaft) {
        this.uml_14_eigenschafts.add(uml_14_eigenschaft);
    }
    public List<UML_14_Verhalten> getUml_14_verhaltens() {
        return uml_14_verhaltens;
    }

    public void addUml_14_verhalten(Uml_14_verhalten uml_14_verhalten) {
        this.uml_14_verhaltens.add(uml_14_verhalten);
    }

}