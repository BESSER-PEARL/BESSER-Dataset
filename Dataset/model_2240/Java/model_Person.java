





import java.util.List;
import java.util.ArrayList;

public class model_Person  {

    private String employmentFactor;
    private String email;
    private String name;
    private String faceUrl;
    private String userName;





    private model_Department model_department;


    public model_Person(
        String employmentFactor,        String email,        String name,        String faceUrl,        String userName    ) {
        this.employmentFactor = employmentFactor;
        this.email = email;
        this.name = name;
        this.faceUrl = faceUrl;
        this.userName = userName;
    }


    public String getEmploymentfactor() {
        return employmentFactor;
    }

    public void setEmploymentfactor(String employmentFactor) {
        this.employmentFactor = employmentFactor;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFaceurl() {
        return faceUrl;
    }

    public void setFaceurl(String faceUrl) {
        this.faceUrl = faceUrl;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }

    public model_Department getModel_department() {
        return model_department;
    }

    public void setModel_department(model_Department model_department) {
        this.model_department = model_department;
    }

}