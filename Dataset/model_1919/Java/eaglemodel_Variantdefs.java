





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Variantdefs  {






    private List<eaglemodel_Variantdef> eaglemodel_variantdefs;




    private eaglemodel_Schematic eaglemodel_schematic;


    public eaglemodel_Variantdefs(
    ) {
        this.eaglemodel_variantdefs = new ArrayList<>();
    }

    public eaglemodel_Variantdefs(
        ArrayList<eaglemodel_Variantdef> eaglemodel_variantdefs    ) {
        this.eaglemodel_variantdefs = eaglemodel_variantdefs;
    }


    public List<eaglemodel_Variantdef> getEaglemodel_variantdefs() {
        return eaglemodel_variantdefs;
    }

    public void addEaglemodel_variantdef(Eaglemodel_variantdef eaglemodel_variantdef) {
        this.eaglemodel_variantdefs.add(eaglemodel_variantdef);
    }
    public eaglemodel_Schematic getEaglemodel_schematic() {
        return eaglemodel_schematic;
    }

    public void setEaglemodel_schematic(eaglemodel_Schematic eaglemodel_schematic) {
        this.eaglemodel_schematic = eaglemodel_schematic;
    }

}