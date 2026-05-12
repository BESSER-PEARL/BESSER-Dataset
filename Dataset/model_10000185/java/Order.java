





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String Type_;
    private int Size_;
    private int ID_;
    private int Quantity;



    public Order(
        String Type_,        int Size_,        int ID_,        int Quantity    ) {
        this.Type_ = Type_;
        this.Size_ = Size_;
        this.ID_ = ID_;
        this.Quantity = Quantity;
    }


    public String getType_() {
        return Type_;
    }

    public void setType_(String Type_) {
        this.Type_ = Type_;
    }
    public int getSize_() {
        return Size_;
    }

    public void setSize_(int Size_) {
        this.Size_ = Size_;
    }
    public int getId_() {
        return ID_;
    }

    public void setId_(int ID_) {
        this.ID_ = ID_;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }


}