





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Compatibility  {






    private eaglemodel_Eagle eaglemodel_eagle;




    private List<eaglemodel_Note> eaglemodel_notes;


    public eaglemodel_Compatibility(
    ) {
        this.eaglemodel_notes = new ArrayList<>();
    }

    public eaglemodel_Compatibility(
        ArrayList<eaglemodel_Note> eaglemodel_notes    ) {
        this.eaglemodel_notes = eaglemodel_notes;
    }


    public eaglemodel_Eagle getEaglemodel_eagle() {
        return eaglemodel_eagle;
    }

    public void setEaglemodel_eagle(eaglemodel_Eagle eaglemodel_eagle) {
        this.eaglemodel_eagle = eaglemodel_eagle;
    }
    public List<eaglemodel_Note> getEaglemodel_notes() {
        return eaglemodel_notes;
    }

    public void addEaglemodel_note(Eaglemodel_note eaglemodel_note) {
        this.eaglemodel_notes.add(eaglemodel_note);
    }

}