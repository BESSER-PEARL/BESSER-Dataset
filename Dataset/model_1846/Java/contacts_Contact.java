





import java.util.List;
import java.util.ArrayList;

public class contacts_Contact  {

    private String company;
    private String title;
    private String image;
    private String webPage;
    private String lastName;
    private String email;
    private String middleName;
    private String note;
    private String jobTitle;
    private String firstName;



    public contacts_Contact(
        String company,        String title,        String image,        String webPage,        String lastName,        String email,        String middleName,        String note,        String jobTitle,        String firstName    ) {
        this.company = company;
        this.title = title;
        this.image = image;
        this.webPage = webPage;
        this.lastName = lastName;
        this.email = email;
        this.middleName = middleName;
        this.note = note;
        this.jobTitle = jobTitle;
        this.firstName = firstName;
    }


    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getWebpage() {
        return webPage;
    }

    public void setWebpage(String webPage) {
        this.webPage = webPage;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getMiddlename() {
        return middleName;
    }

    public void setMiddlename(String middleName) {
        this.middleName = middleName;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getJobtitle() {
        return jobTitle;
    }

    public void setJobtitle(String jobTitle) {
        this.jobTitle = jobTitle;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }


}