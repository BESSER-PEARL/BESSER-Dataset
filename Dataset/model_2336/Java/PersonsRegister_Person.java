





import java.util.List;
import java.util.ArrayList;

public class PersonsRegister_Person  {

    private String identity;
    private String lastName;
    private String firstName;





    private PersonsRegister_PersonsRegister personsregister_personsregister;


    public PersonsRegister_Person(
        String identity,        String lastName,        String firstName    ) {
        this.identity = identity;
        this.lastName = lastName;
        this.firstName = firstName;
    }


    public String getIdentity() {
        return identity;
    }

    public void setIdentity(String identity) {
        this.identity = identity;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public PersonsRegister_PersonsRegister getPersonsregister_personsregister() {
        return personsregister_personsregister;
    }

    public void setPersonsregister_personsregister(PersonsRegister_PersonsRegister personsregister_personsregister) {
        this.personsregister_personsregister = personsregister_personsregister;
    }

}