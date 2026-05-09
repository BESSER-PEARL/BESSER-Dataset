





import java.util.List;
import java.util.ArrayList;

public class analysis_scheduling_FSMCondition  {

    private String valName;
    private String compval;
    private String comp;



    public analysis_scheduling_FSMCondition(
        String valName,        String compval,        String comp    ) {
        this.valName = valName;
        this.compval = compval;
        this.comp = comp;
    }


    public String getValname() {
        return valName;
    }

    public void setValname(String valName) {
        this.valName = valName;
    }
    public String getCompval() {
        return compval;
    }

    public void setCompval(String compval) {
        this.compval = compval;
    }
    public String getComp() {
        return comp;
    }

    public void setComp(String comp) {
        this.comp = comp;
    }


}