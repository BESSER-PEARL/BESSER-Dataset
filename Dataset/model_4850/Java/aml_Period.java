





import java.util.List;
import java.util.ArrayList;

public class aml_Period  {

    private String label;
    private String group;





    private aml_NationState aml_nationstate;




    private aml_DocumentRoot aml_documentroot;




    private List<aml_End> aml_ends;


    public aml_Period(
        String label,        String group    ) {
        this.label = label;
        this.group = group;
        this.aml_ends = new ArrayList<>();
    }

    public aml_Period(
        String label,        String group        ArrayList<aml_End> aml_ends    ) {
        this.label = label;
        this.group = group;
        this.aml_ends = aml_ends;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public aml_NationState getAml_nationstate() {
        return aml_nationstate;
    }

    public void setAml_nationstate(aml_NationState aml_nationstate) {
        this.aml_nationstate = aml_nationstate;
    }
    public aml_DocumentRoot getAml_documentroot() {
        return aml_documentroot;
    }

    public void setAml_documentroot(aml_DocumentRoot aml_documentroot) {
        this.aml_documentroot = aml_documentroot;
    }
    public List<aml_End> getAml_ends() {
        return aml_ends;
    }

    public void addAml_end(Aml_end aml_end) {
        this.aml_ends.add(aml_end);
    }

}