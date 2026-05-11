





import java.util.List;
import java.util.ArrayList;

public class umlMM_Class extends Classifier {

    private String kind;





    private umlMM_Associaton umlmm_associaton;




    private List<umlMM_Associaton> umlmm_associatons;




    private umlMM_Associaton umlmm_associaton;




    private List<umlMM_Associaton> umlmm_associatons;


    public umlMM_Class(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.umlmm_associatons = new ArrayList<>();
        this.umlmm_associatons = new ArrayList<>();
    }

    public umlMM_Class(
        String kind        ArrayList<umlMM_Associaton> umlmm_associatons,        ArrayList<umlMM_Associaton> umlmm_associatons    ) {
        this.kind = kind;
        this.umlmm_associatons = umlmm_associatons;
        this.umlmm_associatons = umlmm_associatons;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public umlMM_Associaton getUmlmm_associaton() {
        return umlmm_associaton;
    }

    public void setUmlmm_associaton(umlMM_Associaton umlmm_associaton) {
        this.umlmm_associaton = umlmm_associaton;
    }
    public List<umlMM_Associaton> getUmlmm_associatons() {
        return umlmm_associatons;
    }

    public void addUmlmm_associaton(Umlmm_associaton umlmm_associaton) {
        this.umlmm_associatons.add(umlmm_associaton);
    }
    public umlMM_Associaton getUmlmm_associaton() {
        return umlmm_associaton;
    }

    public void setUmlmm_associaton(umlMM_Associaton umlmm_associaton) {
        this.umlmm_associaton = umlmm_associaton;
    }
    public List<umlMM_Associaton> getUmlmm_associatons() {
        return umlmm_associatons;
    }

    public void addUmlmm_associaton(Umlmm_associaton umlmm_associaton) {
        this.umlmm_associatons.add(umlmm_associaton);
    }

}