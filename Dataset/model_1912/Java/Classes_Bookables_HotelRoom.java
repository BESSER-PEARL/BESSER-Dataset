





import java.util.List;
import java.util.ArrayList;

public class Classes_Bookables_HotelRoom extends Room {

    private String nbrBeds;
    private String category;



    public Classes_Bookables_HotelRoom(
        String nbrBeds,        String category    ) {
        super(
        );
        this.nbrBeds = nbrBeds;
        this.category = category;
    }


    public String getNbrbeds() {
        return nbrBeds;
    }

    public void setNbrbeds(String nbrBeds) {
        this.nbrBeds = nbrBeds;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }


}