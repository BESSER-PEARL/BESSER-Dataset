





import java.util.List;
import java.util.ArrayList;

public class Hotels  {

    private int name;
    private int id;
    private int hotel_description;





    private Owner owner;


    public Hotels(
        int name,        int id,        int hotel_description    ) {
        this.name = name;
        this.id = id;
        this.hotel_description = hotel_description;
    }


    public int getName() {
        return name;
    }

    public void setName(int name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getHotel_description() {
        return hotel_description;
    }

    public void setHotel_description(int hotel_description) {
        this.hotel_description = hotel_description;
    }

    public Owner getOwner() {
        return owner;
    }

    public void setOwner(Owner owner) {
        this.owner = owner;
    }

}