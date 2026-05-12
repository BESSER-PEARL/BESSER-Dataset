





import java.util.List;
import java.util.ArrayList;

public class SWRC_SoftwareComponent extends Product {

    private String hasPrice;



    public SWRC_SoftwareComponent(
        String hasPrice    ) {
        super(
        );
        this.hasPrice = hasPrice;
    }


    public String getHasprice() {
        return hasPrice;
    }

    public void setHasprice(String hasPrice) {
        this.hasPrice = hasPrice;
    }


}