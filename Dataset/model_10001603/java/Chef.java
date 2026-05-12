





import java.util.List;
import java.util.ArrayList;

public class Chef  {

    private String Speciality;
    private String Chef_name;
    private int Chef_id;
    private String Status;
    private int order_id;



    public Chef(
        String Speciality,        String Chef_name,        int Chef_id,        String Status,        int order_id    ) {
        this.Speciality = Speciality;
        this.Chef_name = Chef_name;
        this.Chef_id = Chef_id;
        this.Status = Status;
        this.order_id = order_id;
    }


    public String getSpeciality() {
        return Speciality;
    }

    public void setSpeciality(String Speciality) {
        this.Speciality = Speciality;
    }
    public String getChef_name() {
        return Chef_name;
    }

    public void setChef_name(String Chef_name) {
        this.Chef_name = Chef_name;
    }
    public int getChef_id() {
        return Chef_id;
    }

    public void setChef_id(int Chef_id) {
        this.Chef_id = Chef_id;
    }
    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public int getOrder_id() {
        return order_id;
    }

    public void setOrder_id(int order_id) {
        this.order_id = order_id;
    }


}