





import java.util.List;
import java.util.ArrayList;

public class petrinetmodel_Transition  {

    private int priority;
    private int token;
    private int id;





    private petrinetmodel_Petrinet petrinetmodel_petrinet;


    public petrinetmodel_Transition(
        int priority,        int token,        int id    ) {
        this.priority = priority;
        this.token = token;
        this.id = id;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
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

    public petrinetmodel_Petrinet getPetrinetmodel_petrinet() {
        return petrinetmodel_petrinet;
    }

    public void setPetrinetmodel_petrinet(petrinetmodel_Petrinet petrinetmodel_petrinet) {
        this.petrinetmodel_petrinet = petrinetmodel_petrinet;
    }

}