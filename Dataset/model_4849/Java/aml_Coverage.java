





import java.util.List;
import java.util.ArrayList;

public class aml_Coverage  {

    private String mixed;
    private String group;





    private List<aml_NationState> aml_nationstates;




    private aml_MetaData aml_metadata;


    public aml_Coverage(
        String mixed,        String group    ) {
        this.mixed = mixed;
        this.group = group;
        this.aml_nationstates = new ArrayList<>();
    }

    public aml_Coverage(
        String mixed,        String group        ArrayList<aml_NationState> aml_nationstates    ) {
        this.mixed = mixed;
        this.group = group;
        this.aml_nationstates = aml_nationstates;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<aml_NationState> getAml_nationstates() {
        return aml_nationstates;
    }

    public void addAml_nationstate(Aml_nationstate aml_nationstate) {
        this.aml_nationstates.add(aml_nationstate);
    }
    public aml_MetaData getAml_metadata() {
        return aml_metadata;
    }

    public void setAml_metadata(aml_MetaData aml_metadata) {
        this.aml_metadata = aml_metadata;
    }

}