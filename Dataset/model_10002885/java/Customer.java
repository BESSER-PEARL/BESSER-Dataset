





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private boolean royalty;
    private String type;



    public Customer(
        boolean royalty,        String type    ) {
        this.royalty = royalty;
        this.type = type;
    }


    public boolean getRoyalty() {
        return royalty;
    }

    public void setRoyalty(boolean royalty) {
        this.royalty = royalty;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}