





import java.util.List;
import java.util.ArrayList;

public class petrinetmodel_Place  {

    private int token;
    private int id;





    private petrinetmodel_Transition petrinetmodel_transition;




    private petrinetmodel_Petrinet petrinetmodel_petrinet;


    public petrinetmodel_Place(
        int token,        int id    ) {
        this.token = token;
        this.id = id;
    }


    public int getToken() {
        return token;
    }

    public void setToken(int token) {
        this.token = token;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public petrinetmodel_Transition getPetrinetmodel_transition() {
        return petrinetmodel_transition;
    }

    public void setPetrinetmodel_transition(petrinetmodel_Transition petrinetmodel_transition) {
        this.petrinetmodel_transition = petrinetmodel_transition;
    }
    public petrinetmodel_Petrinet getPetrinetmodel_petrinet() {
        return petrinetmodel_petrinet;
    }

    public void setPetrinetmodel_petrinet(petrinetmodel_Petrinet petrinetmodel_petrinet) {
        this.petrinetmodel_petrinet = petrinetmodel_petrinet;
    }

}