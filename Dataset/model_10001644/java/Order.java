





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String Type_;
    private int Quantity;
    private int Size_;
    private int ID_;



    public Order(
        String Type_,        int Quantity,        int Size_,        int ID_    ) {
        this.Type_ = Type_;
        this.Quantity = Quantity;
        this.Size_ = Size_;
        this.ID_ = ID_;
    }


    public String getType_() {
        return Type_;
    }

    public void setType_(String Type_) {
        this.Type_ = Type_;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
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


}