





import java.util.List;
import java.util.ArrayList;

public class corprateClient  {

    private String client_name;
    private int phone;
    private int companyRate;
    private int client_ID;





    private Course course;


    public corprateClient(
        String client_name,        int phone,        int companyRate,        int client_ID    ) {
        this.client_name = client_name;
        this.phone = phone;
        this.companyRate = companyRate;
        this.client_ID = client_ID;
    }


    public String getClient_name() {
        return client_name;
    }

    public void setClient_name(String client_name) {
        this.client_name = client_name;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public int getCompanyrate() {
        return companyRate;
    }

    public void setCompanyrate(int companyRate) {
        this.companyRate = companyRate;
    }
    public int getClient_id() {
        return client_ID;
    }

    public void setClient_id(int client_ID) {
        this.client_ID = client_ID;
    }

    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
        this.course = course;
    }

}