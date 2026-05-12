





import java.util.List;
import java.util.ArrayList;

public class medicine  {

    private int id;
    private int price;
    private String medicine;



    public medicine(
        int id,        int price,        String medicine    ) {
        this.id = id;
        this.price = price;
        this.medicine = medicine;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getMedicine() {
        return medicine;
    }

    public void setMedicine(String medicine) {
        this.medicine = medicine;
    }


}