





import java.util.List;
import java.util.ArrayList;

public class customer  {

    private int id_card;
    private String name;
    private String address;





    private the_product the_product;


    public customer(
        int id_card,        String name,        String address    ) {
        this.id_card = id_card;
        this.name = name;
        this.address = address;
    }


    public int getId_card() {
        return id_card;
    }

    public void setId_card(int id_card) {
        this.id_card = id_card;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public the_product getThe_product() {
        return the_product;
    }

    public void setThe_product(the_product the_product) {
        this.the_product = the_product;
    }

}