





import java.util.List;
import java.util.ArrayList;

public class model_Book  {

    private String data;
    private String title;
    private String tags;





    private List<model_Person> model_persons;




    private model_Person model_person;


    public model_Book(
        String data,        String title,        String tags    ) {
        this.data = data;
        this.title = title;
        this.tags = tags;
        this.model_persons = new ArrayList<>();
    }

    public model_Book(
        String data,        String title,        String tags        ArrayList<model_Person> model_persons    ) {
        this.data = data;
        this.title = title;
        this.tags = tags;
        this.model_persons = model_persons;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getTags() {
        return tags;
    }

    public void setTags(String tags) {
        this.tags = tags;
    }

    public List<model_Person> getModel_persons() {
        return model_persons;
    }

    public void addModel_person(Model_person model_person) {
        this.model_persons.add(model_person);
    }
    public model_Person getModel_person() {
        return model_person;
    }

    public void setModel_person(model_Person model_person) {
        this.model_person = model_person;
    }

}