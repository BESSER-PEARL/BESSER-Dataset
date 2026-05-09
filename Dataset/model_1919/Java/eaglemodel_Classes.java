





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Classes  {






    private List<eaglemodel_Class> eaglemodel_classs;




    private eaglemodel_Schematic eaglemodel_schematic;


    public eaglemodel_Classes(
    ) {
        this.eaglemodel_classs = new ArrayList<>();
    }

    public eaglemodel_Classes(
        ArrayList<eaglemodel_Class> eaglemodel_classs    ) {
        this.eaglemodel_classs = eaglemodel_classs;
    }


    public List<eaglemodel_Class> getEaglemodel_classs() {
        return eaglemodel_classs;
    }

    public void addEaglemodel_class(Eaglemodel_class eaglemodel_class) {
        this.eaglemodel_classs.add(eaglemodel_class);
    }
    public eaglemodel_Schematic getEaglemodel_schematic() {
        return eaglemodel_schematic;
    }

    public void setEaglemodel_schematic(eaglemodel_Schematic eaglemodel_schematic) {
        this.eaglemodel_schematic = eaglemodel_schematic;
    }

}