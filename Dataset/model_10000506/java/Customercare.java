





import java.util.List;
import java.util.ArrayList;

public class Customercare  {

    private String address;
    private int no;





    private List<Buyer> buyers;


    public Customercare(
        String address,        int no    ) {
        this.address = address;
        this.no = no;
        this.buyers = new ArrayList<>();
    }

    public Customercare(
        String address,        int no        ArrayList<Buyer> buyers    ) {
        this.address = address;
        this.no = no;
        this.buyers = buyers;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }

    public List<Buyer> getBuyers() {
        return buyers;
    }

    public void addBuyer(Buyer buyer) {
        this.buyers.add(buyer);
    }

}