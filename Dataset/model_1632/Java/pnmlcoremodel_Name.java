





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Name extends Label {

    private String text;





    private pnmlcoremodel_Object pnmlcoremodel_object;




    private pnmlcoremodel_PetriNet pnmlcoremodel_petrinet;


    public pnmlcoremodel_Name(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public pnmlcoremodel_Object getPnmlcoremodel_object() {
        return pnmlcoremodel_object;
    }

    public void setPnmlcoremodel_object(pnmlcoremodel_Object pnmlcoremodel_object) {
        this.pnmlcoremodel_object = pnmlcoremodel_object;
    }
    public pnmlcoremodel_PetriNet getPnmlcoremodel_petrinet() {
        return pnmlcoremodel_petrinet;
    }

    public void setPnmlcoremodel_petrinet(pnmlcoremodel_PetriNet pnmlcoremodel_petrinet) {
        this.pnmlcoremodel_petrinet = pnmlcoremodel_petrinet;
    }

}