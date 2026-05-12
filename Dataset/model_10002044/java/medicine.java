





import java.util.List;
import java.util.ArrayList;

public class medicine  {

    private String m_name;
    private int quantity;
    private float price;
    private int m_code;





    private Doctor doctor;




    private Bill bill;


    public medicine(
        String m_name,        int quantity,        float price,        int m_code    ) {
        this.m_name = m_name;
        this.quantity = quantity;
        this.price = price;
        this.m_code = m_code;
    }


    public String getM_name() {
        return m_name;
    }

    public void setM_name(String m_name) {
        this.m_name = m_name;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getM_code() {
        return m_code;
    }

    public void setM_code(int m_code) {
        this.m_code = m_code;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }
    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }

}