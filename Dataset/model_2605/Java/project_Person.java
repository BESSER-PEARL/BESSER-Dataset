





import java.util.List;
import java.util.ArrayList;

public class project_Person  {

    private String email;
    private String image;
    private String lastname;
    private String firstname;





    private project_Foundation project_foundation;




    private project_Project project_project;


    public project_Person(
        String email,        String image,        String lastname,        String firstname    ) {
        this.email = email;
        this.image = image;
        this.lastname = lastname;
        this.firstname = firstname;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public project_Foundation getProject_foundation() {
        return project_foundation;
    }

    public void setProject_foundation(project_Foundation project_foundation) {
        this.project_foundation = project_foundation;
    }
    public project_Project getProject_project() {
        return project_project;
    }

    public void setProject_project(project_Project project_project) {
        this.project_project = project_project;
    }

}