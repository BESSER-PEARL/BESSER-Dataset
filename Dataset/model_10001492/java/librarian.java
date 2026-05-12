




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class librarian  {

    private String email;
    private LocalDate birth_date;
    private String name;
    private LocalDate hire_date;
    private String job;
    private String address;
    private int id;





    private user user;


    public librarian(
        String email,        LocalDate birth_date,        String name,        LocalDate hire_date,        String job,        String address,        int id    ) {
        this.email = email;
        this.birth_date = birth_date;
        this.name = name;
        this.hire_date = hire_date;
        this.job = job;
        this.address = address;
        this.id = id;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public LocalDate getBirth_date() {
        return birth_date;
    }

    public void setBirth_date(LocalDate birth_date) {
        this.birth_date = birth_date;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getHire_date() {
        return hire_date;
    }

    public void setHire_date(LocalDate hire_date) {
        this.hire_date = hire_date;
    }
    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}