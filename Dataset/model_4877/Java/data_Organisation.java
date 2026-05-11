





import java.util.List;
import java.util.ArrayList;

public class data_Organisation extends InformationObject {






    private data_Person data_person;




    private data_Organisation data_organisation;




    private data_Person data_person;




    private data_Organisation data_organisation;




    private data_Person data_person;




    private List<data_Person> data_persons;


    public data_Organisation(
    ) {
        super(
        );
        this.data_persons = new ArrayList<>();
    }

    public data_Organisation(
        ArrayList<data_Person> data_persons    ) {
        this.data_persons = data_persons;
    }


    public data_Person getData_person() {
        return data_person;
    }

    public void setData_person(data_Person data_person) {
        this.data_person = data_person;
    }
    public data_Organisation getData_organisation() {
        return data_organisation;
    }

    public void setData_organisation(data_Organisation data_organisation) {
        this.data_organisation = data_organisation;
    }
    public data_Person getData_person() {
        return data_person;
    }

    public void setData_person(data_Person data_person) {
        this.data_person = data_person;
    }
    public data_Organisation getData_organisation() {
        return data_organisation;
    }

    public void setData_organisation(data_Organisation data_organisation) {
        this.data_organisation = data_organisation;
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

}