





import java.util.List;
import java.util.ArrayList;

public class ram_Aspect extends NamedElement {






    private List<ram_Instantiation> ram_instantiations;




    private ram_Instantiation ram_instantiation;




    private ram_Layout ram_layout;




    private List<ram_AbstractMessageView> ram_abstractmessageviews;




    private List<ram_MappableElement> ram_mappableelements;


    public ram_Aspect(
    ) {
        super(
        );
        this.ram_instantiations = new ArrayList<>();
        this.ram_abstractmessageviews = new ArrayList<>();
        this.ram_mappableelements = new ArrayList<>();
    }

    public ram_Aspect(
        ArrayList<ram_Instantiation> ram_instantiations,        ArrayList<ram_AbstractMessageView> ram_abstractmessageviews,        ArrayList<ram_MappableElement> ram_mappableelements    ) {
        this.ram_instantiations = ram_instantiations;
        this.ram_abstractmessageviews = ram_abstractmessageviews;
        this.ram_mappableelements = ram_mappableelements;
    }


    public List<ram_Instantiation> getRam_instantiations() {
        return ram_instantiations;
    }

    public void addRam_instantiation(Ram_instantiation ram_instantiation) {
        this.ram_instantiations.add(ram_instantiation);
    }
    public ram_Instantiation getRam_instantiation() {
        return ram_instantiation;
    }

    public void setRam_instantiation(ram_Instantiation ram_instantiation) {
        this.ram_instantiation = ram_instantiation;
    }
    public ram_Layout getRam_layout() {
        return ram_layout;
    }

    public void setRam_layout(ram_Layout ram_layout) {
        this.ram_layout = ram_layout;
    }
    public List<ram_AbstractMessageView> getRam_abstractmessageviews() {
        return ram_abstractmessageviews;
    }

    public void addRam_abstractmessageview(Ram_abstractmessageview ram_abstractmessageview) {
        this.ram_abstractmessageviews.add(ram_abstractmessageview);
    }
    public List<ram_MappableElement> getRam_mappableelements() {
        return ram_mappableelements;
    }

    public void addRam_mappableelement(Ram_mappableelement ram_mappableelement) {
        this.ram_mappableelements.add(ram_mappableelement);
    }

}