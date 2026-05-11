





import java.util.List;
import java.util.ArrayList;

public class sample_A  {

    private int quantity;
    private boolean valid;
    private String name;



    public sample_A(
        int quantity,        boolean valid,        String name    ) {
        this.quantity = quantity;
        this.valid = valid;
        this.name = name;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public boolean getValid() {
        return valid;
    }

    public void setValid(boolean valid) {
        this.valid = valid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}