




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class edu_Student  {

    private int id;
    private LocalDate date_of_birth;
    private String name;



    public edu_Student(
        int id,        LocalDate date_of_birth,        String name    ) {
        this.id = id;
        this.date_of_birth = date_of_birth;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getDate_of_birth() {
        return date_of_birth;
    }

    public void setDate_of_birth(LocalDate date_of_birth) {
        this.date_of_birth = date_of_birth;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}