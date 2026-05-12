





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String Address;
    private int Age;
    private String Prescriptions;
    private String Phone;
    private String DiseaseHistory;



    public Patient(
        String Address,        int Age,        String Prescriptions,        String Phone,        String DiseaseHistory    ) {
        this.Address = Address;
        this.Age = Age;
        this.Prescriptions = Prescriptions;
        this.Phone = Phone;
        this.DiseaseHistory = DiseaseHistory;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getPrescriptions() {
        return Prescriptions;
    }

    public void setPrescriptions(String Prescriptions) {
        this.Prescriptions = Prescriptions;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getDiseasehistory() {
        return DiseaseHistory;
    }

    public void setDiseasehistory(String DiseaseHistory) {
        this.DiseaseHistory = DiseaseHistory;
    }


}