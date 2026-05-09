





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Sheets  {






    private List<eaglemodel_Sheet> eaglemodel_sheets;




    private eaglemodel_Schematic eaglemodel_schematic;


    public eaglemodel_Sheets(
    ) {
        this.eaglemodel_sheets = new ArrayList<>();
    }

    public eaglemodel_Sheets(
        ArrayList<eaglemodel_Sheet> eaglemodel_sheets    ) {
        this.eaglemodel_sheets = eaglemodel_sheets;
    }


    public List<eaglemodel_Sheet> getEaglemodel_sheets() {
        return eaglemodel_sheets;
    }

    public void addEaglemodel_sheet(Eaglemodel_sheet eaglemodel_sheet) {
        this.eaglemodel_sheets.add(eaglemodel_sheet);
    }
    public eaglemodel_Schematic getEaglemodel_schematic() {
        return eaglemodel_schematic;
    }

    public void setEaglemodel_schematic(eaglemodel_Schematic eaglemodel_schematic) {
        this.eaglemodel_schematic = eaglemodel_schematic;
    }

}