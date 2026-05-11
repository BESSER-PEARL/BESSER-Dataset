





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Location extends Element {






    private contentfwk_Location contentfwk_location;




    private List<contentfwk_Location> contentfwk_locations;


    public contentfwk_Location(
    ) {
        super(
        );
        this.contentfwk_locations = new ArrayList<>();
    }

    public contentfwk_Location(
        ArrayList<contentfwk_Location> contentfwk_locations    ) {
        this.contentfwk_locations = contentfwk_locations;
    }


    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public List<contentfwk_Location> getContentfwk_locations() {
        return contentfwk_locations;
    }

    public void addContentfwk_location(Contentfwk_location contentfwk_location) {
        this.contentfwk_locations.add(contentfwk_location);
    }

}