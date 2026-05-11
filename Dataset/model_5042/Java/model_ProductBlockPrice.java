





import java.util.List;
import java.util.ArrayList;

public class model_ProductBlockPrice extends IEntity {

    private String block;
    private String price;



    public model_ProductBlockPrice(
        String block,        String price    ) {
        super(
        );
        this.block = block;
        this.price = price;
    }


    public String getBlock() {
        return block;
    }

    public void setBlock(String block) {
        this.block = block;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }


}