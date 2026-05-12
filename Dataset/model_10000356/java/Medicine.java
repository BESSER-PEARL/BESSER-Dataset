





import java.util.List;
import java.util.ArrayList;

public class Medicine  {

    private String price;
    private int amount;
    private int code;
    private String name;





    private Doctor doctor;


    public Medicine(
        String price,        int amount,        int code,        String name    ) {
        this.price = price;
        this.amount = amount;
        this.code = code;
        this.name = name;
    }


    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}