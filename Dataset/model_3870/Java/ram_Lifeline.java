





import java.util.List;
import java.util.ArrayList;

public class ram_Lifeline  {






    private ram_Interaction ram_interaction;




    private ram_TypedElement ram_typedelement;




    private List<ram_TemporaryProperty> ram_temporarypropertys;


    public ram_Lifeline(
    ) {
        this.ram_temporarypropertys = new ArrayList<>();
    }

    public ram_Lifeline(
        ArrayList<ram_TemporaryProperty> ram_temporarypropertys    ) {
        this.ram_temporarypropertys = ram_temporarypropertys;
    }


    public ram_Interaction getRam_interaction() {
        return ram_interaction;
    }

    public void setRam_interaction(ram_Interaction ram_interaction) {
        this.ram_interaction = ram_interaction;
    }
    public ram_TypedElement getRam_typedelement() {
        return ram_typedelement;
    }

    public void setRam_typedelement(ram_TypedElement ram_typedelement) {
        this.ram_typedelement = ram_typedelement;
    }
    public List<ram_TemporaryProperty> getRam_temporarypropertys() {
        return ram_temporarypropertys;
    }

    public void addRam_temporaryproperty(Ram_temporaryproperty ram_temporaryproperty) {
        this.ram_temporarypropertys.add(ram_temporaryproperty);
    }

}