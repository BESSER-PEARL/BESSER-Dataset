





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Errors  {






    private eaglemodel_Schematic eaglemodel_schematic;




    private List<eaglemodel_Approved> eaglemodel_approveds;


    public eaglemodel_Errors(
    ) {
        this.eaglemodel_approveds = new ArrayList<>();
    }

    public eaglemodel_Errors(
        ArrayList<eaglemodel_Approved> eaglemodel_approveds    ) {
        this.eaglemodel_approveds = eaglemodel_approveds;
    }


    public eaglemodel_Schematic getEaglemodel_schematic() {
        return eaglemodel_schematic;
    }

    public void setEaglemodel_schematic(eaglemodel_Schematic eaglemodel_schematic) {
        this.eaglemodel_schematic = eaglemodel_schematic;
    }
    public List<eaglemodel_Approved> getEaglemodel_approveds() {
        return eaglemodel_approveds;
    }

    public void addEaglemodel_approved(Eaglemodel_approved eaglemodel_approved) {
        this.eaglemodel_approveds.add(eaglemodel_approved);
    }

}