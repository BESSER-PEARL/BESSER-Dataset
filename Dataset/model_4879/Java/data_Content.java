





import java.util.List;
import java.util.ArrayList;

public class data_Content extends InformationObject {

    private String locale;





    private data_Person data_person;




    private List<data_Person> data_persons;




    private data_Content data_content;




    private data_Person data_person;




    private data_Content data_content;




    private data_Person data_person;


    public data_Content(
        String locale    ) {
        super(
        );
        this.locale = locale;
        this.data_persons = new ArrayList<>();
    }

    public data_Content(
        String locale        ArrayList<data_Person> data_persons    ) {
        this.locale = locale;
        this.data_persons = data_persons;
    }

    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }

    public data_Person getData_person() {
        return data_person;
    }

    public void setData_person(data_Person data_person) {
        this.data_person = data_person;
    }
    public List<data_Person> getData_persons() {
        return data_persons;
    }

    public void addData_person(Data_person data_person) {
        this.data_persons.add(data_person);
    }
    public data_Content getData_content() {
        return data_content;
    }

    public void setData_content(data_Content data_content) {
        this.data_content = data_content;
    }
    public data_Person getData_person() {
        return data_person;
    }

    public void setData_person(data_Person data_person) {
        this.data_person = data_person;
    }
    public data_Content getData_content() {
        return data_content;
    }

    public void setData_content(data_Content data_content) {
        this.data_content = data_content;
    }
    public data_Person getData_person() {
        return data_person;
    }

    public void setData_person(data_Person data_person) {
        this.data_person = data_person;
    }

}