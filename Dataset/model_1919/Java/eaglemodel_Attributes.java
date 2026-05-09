





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Attributes  {






    private eaglemodel_Schematic eaglemodel_schematic;




    private List<eaglemodel_Attribute> eaglemodel_attributes;


    public eaglemodel_Attributes(
    ) {
        this.eaglemodel_attributes = new ArrayList<>();
    }

    public eaglemodel_Attributes(
        ArrayList<eaglemodel_Attribute> eaglemodel_attributes    ) {
        this.eaglemodel_attributes = eaglemodel_attributes;
    }


    public eaglemodel_Schematic getEaglemodel_schematic() {
        return eaglemodel_schematic;
    }

    public void setEaglemodel_schematic(eaglemodel_Schematic eaglemodel_schematic) {
        this.eaglemodel_schematic = eaglemodel_schematic;
    }
    public List<eaglemodel_Attribute> getEaglemodel_attributes() {
        return eaglemodel_attributes;
    }

    public void addEaglemodel_attribute(Eaglemodel_attribute eaglemodel_attribute) {
        this.eaglemodel_attributes.add(eaglemodel_attribute);
    }

}