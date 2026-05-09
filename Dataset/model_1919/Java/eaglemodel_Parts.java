





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Parts  {






    private eaglemodel_Schematic eaglemodel_schematic;




    private List<eaglemodel_Part> eaglemodel_parts;


    public eaglemodel_Parts(
    ) {
        this.eaglemodel_parts = new ArrayList<>();
    }

    public eaglemodel_Parts(
        ArrayList<eaglemodel_Part> eaglemodel_parts    ) {
        this.eaglemodel_parts = eaglemodel_parts;
    }


    public eaglemodel_Schematic getEaglemodel_schematic() {
        return eaglemodel_schematic;
    }

    public void setEaglemodel_schematic(eaglemodel_Schematic eaglemodel_schematic) {
        this.eaglemodel_schematic = eaglemodel_schematic;
    }
    public List<eaglemodel_Part> getEaglemodel_parts() {
        return eaglemodel_parts;
    }

    public void addEaglemodel_part(Eaglemodel_part eaglemodel_part) {
        this.eaglemodel_parts.add(eaglemodel_part);
    }

}