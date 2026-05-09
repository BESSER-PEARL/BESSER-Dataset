





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_miniOCL_ForAllExpCS extends LoopExpCS {






    private List<AccVarCS> accvarcss;


    public mutatorenvironment_miniOCL_ForAllExpCS(
    ) {
        super(
        );
        this.accvarcss = new ArrayList<>();
    }

    public mutatorenvironment_miniOCL_ForAllExpCS(
        ArrayList<AccVarCS> accvarcss    ) {
        this.accvarcss = accvarcss;
    }


    public List<AccVarCS> getAccvarcss() {
        return accvarcss;
    }

    public void addAccvarcs(Accvarcs accvarcs) {
        this.accvarcss.add(accvarcs);
    }

}