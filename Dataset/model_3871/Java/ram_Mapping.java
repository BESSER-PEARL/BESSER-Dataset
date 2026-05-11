





import java.util.List;
import java.util.ArrayList;

public class ram_Mapping  {






    private ram_Instantiation ram_instantiation;




    private List<ram_MappableElement> ram_mappableelements;




    private ram_MappableElement ram_mappableelement;


    public ram_Mapping(
    ) {
        this.ram_mappableelements = new ArrayList<>();
    }

    public ram_Mapping(
        ArrayList<ram_MappableElement> ram_mappableelements    ) {
        this.ram_mappableelements = ram_mappableelements;
    }


    public ram_Instantiation getRam_instantiation() {
        return ram_instantiation;
    }

    public void setRam_instantiation(ram_Instantiation ram_instantiation) {
        this.ram_instantiation = ram_instantiation;
    }
    public List<ram_MappableElement> getRam_mappableelements() {
        return ram_mappableelements;
    }

    public void addRam_mappableelement(Ram_mappableelement ram_mappableelement) {
        this.ram_mappableelements.add(ram_mappableelement);
    }
    public ram_MappableElement getRam_mappableelement() {
        return ram_mappableelement;
    }

    public void setRam_mappableelement(ram_MappableElement ram_mappableelement) {
        this.ram_mappableelement = ram_mappableelement;
    }

}