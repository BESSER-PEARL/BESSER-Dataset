





import java.util.List;
import java.util.ArrayList;

public class customer  {

    private String name;
    private int addresstobill;
    private int addresstoship;





    private creditcard creditcard;


    public customer(
        String name,        int addresstobill,        int addresstoship    ) {
        this.name = name;
        this.addresstobill = addresstobill;
        this.addresstoship = addresstoship;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAddresstobill() {
        return addresstobill;
    }

    public void setAddresstobill(int addresstobill) {
        this.addresstobill = addresstobill;
    }
    public int getAddresstoship() {
        return addresstoship;
    }

    public void setAddresstoship(int addresstoship) {
        this.addresstoship = addresstoship;
    }

    public creditcard getCreditcard() {
        return creditcard;
    }

    public void setCreditcard(creditcard creditcard) {
        this.creditcard = creditcard;
    }

}