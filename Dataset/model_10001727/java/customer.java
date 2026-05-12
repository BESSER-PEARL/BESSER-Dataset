





import java.util.List;
import java.util.ArrayList;

public class customer  {

    private int addresstoship;
    private int addresstobill;
    private String name;





    private creditcard creditcard;


    public customer(
        int addresstoship,        int addresstobill,        String name    ) {
        this.addresstoship = addresstoship;
        this.addresstobill = addresstobill;
        this.name = name;
    }


    public int getAddresstoship() {
        return addresstoship;
    }

    public void setAddresstoship(int addresstoship) {
        this.addresstoship = addresstoship;
    }
    public int getAddresstobill() {
        return addresstobill;
    }

    public void setAddresstobill(int addresstobill) {
        this.addresstobill = addresstobill;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public creditcard getCreditcard() {
        return creditcard;
    }

    public void setCreditcard(creditcard creditcard) {
        this.creditcard = creditcard;
    }

}