





import java.util.List;
import java.util.ArrayList;

public class NQC_Program  {

    private String Name;





    private List<NQC_GlobalVariable> nqc_globalvariables;


    public NQC_Program(
        String Name    ) {
        this.Name = Name;
        this.nqc_globalvariables = new ArrayList<>();
    }

    public NQC_Program(
        String Name        ArrayList<NQC_GlobalVariable> nqc_globalvariables    ) {
        this.Name = Name;
        this.nqc_globalvariables = nqc_globalvariables;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<NQC_GlobalVariable> getNqc_globalvariables() {
        return nqc_globalvariables;
    }

    public void addNqc_globalvariable(Nqc_globalvariable nqc_globalvariable) {
        this.nqc_globalvariables.add(nqc_globalvariable);
    }

}