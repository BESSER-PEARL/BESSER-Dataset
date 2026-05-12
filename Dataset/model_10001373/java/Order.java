





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String Type;
    private int Quantity;
    private int Size;
    private int ID;



    public Order(
        String Type,        int Quantity,        int Size,        int ID    ) {
        this.Type = Type;
        this.Quantity = Quantity;
        this.Size = Size;
        this.ID = ID;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getSize() {
        return Size;
    }

    public void setSize(int Size) {
        this.Size = Size;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }


}