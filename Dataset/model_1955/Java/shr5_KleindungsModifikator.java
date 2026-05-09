





import java.util.List;
import java.util.ArrayList;

public class shr5_KleindungsModifikator extends Quelle, Beschreibbar, GeldWert {

    private int capacity;
    private int rating;
    private String type;



    public shr5_KleindungsModifikator(
        int capacity,        int rating,        String type    ) {
        super(
        );
        this.capacity = capacity;
        this.rating = rating;
        this.type = type;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}