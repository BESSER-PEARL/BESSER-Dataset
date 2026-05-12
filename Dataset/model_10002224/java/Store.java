





import java.util.List;
import java.util.ArrayList;

public class Store  {

    private String name;
    private String photoPath;
    private int id;





    private Address address;




    private Seller seller;


    public Store(
        String name,        String photoPath,        int id    ) {
        this.name = name;
        this.photoPath = photoPath;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhotopath() {
        return photoPath;
    }

    public void setPhotopath(String photoPath) {
        this.photoPath = photoPath;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }
    public Seller getSeller() {
        return seller;
    }

    public void setSeller(Seller seller) {
        this.seller = seller;
    }

}