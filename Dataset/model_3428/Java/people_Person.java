





import java.util.List;
import java.util.ArrayList;

public class people_Person  {

    private String name;





    private people_Model people_model;


    public people_Person(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public people_Model getPeople_model() {
        return people_model;
    }

    public void setPeople_model(people_Model people_model) {
        this.people_model = people_model;
    }

}