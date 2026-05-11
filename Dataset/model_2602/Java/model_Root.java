





import java.util.List;
import java.util.ArrayList;

public class model_Root  {






    private List<model_Person> model_persons;




    private model_PersonList model_personlist;


    public model_Root(
    ) {
        this.model_persons = new ArrayList<>();
    }

    public model_Root(
        ArrayList<model_Person> model_persons    ) {
        this.model_persons = model_persons;
    }


    public List<model_Person> getModel_persons() {
        return model_persons;
    }

    public void addModel_person(Model_person model_person) {
        this.model_persons.add(model_person);
    }
    public model_PersonList getModel_personlist() {
        return model_personlist;
    }

    public void setModel_personlist(model_PersonList model_personlist) {
        this.model_personlist = model_personlist;
    }

}