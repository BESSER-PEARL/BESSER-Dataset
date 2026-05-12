





import java.util.List;
import java.util.ArrayList;

public class Store  {

    private String photoPath;
    private String name;
    private int id;





    private Seller seller;




    private Address address;


    public Store(
        String photoPath,        String name,        int id    ) {
        this.photoPath = photoPath;
        this.name = name;
        this.id = id;
    }


    public String getPhotopath() {
        return photoPath;
    }

    public void setPhotopath(String photoPath) {
        this.photoPath = photoPath;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Seller getSeller() {
        return seller;
    }

    public void setSeller(Seller seller) {
        this.seller = seller;
    }
    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }

}