





import java.util.List;
import java.util.ArrayList;

public class model_Book  {

    private String tags;
    private String title;
    private String data;





    private model_Location model_location;




    private model_MappedLibrary model_mappedlibrary;




    private model_Person model_person;




    private List<model_Person> model_persons;




    private model_MappedLibrary model_mappedlibrary;


    public model_Book(
        String tags,        String title,        String data    ) {
        this.tags = tags;
        this.title = title;
        this.data = data;
        this.model_persons = new ArrayList<>();
    }

    public model_Book(
        String tags,        String title,        String data        ArrayList<model_Person> model_persons    ) {
        this.tags = tags;
        this.title = title;
        this.data = data;
        this.model_persons = model_persons;
    }

    public String getTags() {
        return tags;
    }

    public void setTags(String tags) {
        this.tags = tags;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public model_Location getModel_location() {
        return model_location;
    }

    public void setModel_location(model_Location model_location) {
        this.model_location = model_location;
    }
    public model_MappedLibrary getModel_mappedlibrary() {
        return model_mappedlibrary;
    }

    public void setModel_mappedlibrary(model_MappedLibrary model_mappedlibrary) {
        this.model_mappedlibrary = model_mappedlibrary;
    }
    public model_Person getModel_person() {
        return model_person;
    }

    public void setModel_person(model_Person model_person) {
        this.model_person = model_person;
    }
    public List<model_Person> getModel_persons() {
        return model_persons;
    }

    public void addModel_person(Model_person model_person) {
        this.model_persons.add(model_person);
    }
    public model_MappedLibrary getModel_mappedlibrary() {
        return model_mappedlibrary;
    }

    public void setModel_mappedlibrary(model_MappedLibrary model_mappedlibrary) {
        this.model_mappedlibrary = model_mappedlibrary;
    }

}