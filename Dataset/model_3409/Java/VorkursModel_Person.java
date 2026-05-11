





import java.util.List;
import java.util.ArrayList;

public class VorkursModel_Person  {

    private String gender;
    private String firstname;
    private String subject;
    private String lastname;





    private VorkursModel_Notebook vorkursmodel_notebook;




    private VorkursModel_Qualification vorkursmodel_qualification;


    public VorkursModel_Person(
        String gender,        String firstname,        String subject,        String lastname    ) {
        this.gender = gender;
        this.firstname = firstname;
        this.subject = subject;
        this.lastname = lastname;
    }


    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public VorkursModel_Notebook getVorkursmodel_notebook() {
        return vorkursmodel_notebook;
    }

    public void setVorkursmodel_notebook(VorkursModel_Notebook vorkursmodel_notebook) {
        this.vorkursmodel_notebook = vorkursmodel_notebook;
    }
    public VorkursModel_Qualification getVorkursmodel_qualification() {
        return vorkursmodel_qualification;
    }

    public void setVorkursmodel_qualification(VorkursModel_Qualification vorkursmodel_qualification) {
        this.vorkursmodel_qualification = vorkursmodel_qualification;
    }

}