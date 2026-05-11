





import java.util.List;
import java.util.ArrayList;

public class avm_DistributionRestriction  {

    private String Notes;





    private avm_Component avm_component;


    public avm_DistributionRestriction(
        String Notes    ) {
        this.Notes = Notes;
    }


    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }

    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }

}