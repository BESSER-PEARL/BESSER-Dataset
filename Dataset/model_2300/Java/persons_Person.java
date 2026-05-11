




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class persons_Person  {

    private String fullName;
    private LocalDate birthday;





    private persons_PersonRegister persons_personregister;


    public persons_Person(
        String fullName,        LocalDate birthday    ) {
        this.fullName = fullName;
        this.birthday = birthday;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public LocalDate getBirthday() {
        return birthday;
    }

    public void setBirthday(LocalDate birthday) {
        this.birthday = birthday;
    }

    public persons_PersonRegister getPersons_personregister() {
        return persons_personregister;
    }

    public void setPersons_personregister(persons_PersonRegister persons_personregister) {
        this.persons_personregister = persons_personregister;
    }

}