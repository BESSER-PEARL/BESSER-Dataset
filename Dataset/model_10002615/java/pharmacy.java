





import java.util.List;
import java.util.ArrayList;

public class pharmacy  {

    private String medicine;
    private int price;





    private Patient patient;




    private Bursar bursar;


    public pharmacy(
        String medicine,        int price    ) {
        this.medicine = medicine;
        this.price = price;
    }


    public String getMedicine() {
        return medicine;
    }

    public void setMedicine(String medicine) {
        this.medicine = medicine;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public Bursar getBursar() {
        return bursar;
    }

    public void setBursar(Bursar bursar) {
        this.bursar = bursar;
    }

}