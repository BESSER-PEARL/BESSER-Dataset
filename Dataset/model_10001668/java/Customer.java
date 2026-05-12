





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String type;
    private boolean royalty;



    public Customer(
        String type,        boolean royalty    ) {
        this.type = type;
        this.royalty = royalty;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getRoyalty() {
        return royalty;
    }

    public void setRoyalty(boolean royalty) {
        this.royalty = royalty;
    }


}