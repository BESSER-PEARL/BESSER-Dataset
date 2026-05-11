





import java.util.List;
import java.util.ArrayList;

public class delphi_setConstructor extends CSTrace {






    private delphi_factor delphi_factor;




    private List<delphi_setElement> delphi_setelements;


    public delphi_setConstructor(
    ) {
        super(
        );
        this.delphi_setelements = new ArrayList<>();
    }

    public delphi_setConstructor(
        ArrayList<delphi_setElement> delphi_setelements    ) {
        this.delphi_setelements = delphi_setelements;
    }


    public delphi_factor getDelphi_factor() {
        return delphi_factor;
    }

    public void setDelphi_factor(delphi_factor delphi_factor) {
        this.delphi_factor = delphi_factor;
    }
    public List<delphi_setElement> getDelphi_setelements() {
        return delphi_setelements;
    }

    public void addDelphi_setelement(Delphi_setelement delphi_setelement) {
        this.delphi_setelements.add(delphi_setelement);
    }

}