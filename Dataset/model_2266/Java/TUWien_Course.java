





import java.util.List;
import java.util.ArrayList;

public class TUWien_Course  {

    private String name;
    private String id;





    private TUWien_University tuwien_university;


    public TUWien_Course(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public TUWien_University getTuwien_university() {
        return tuwien_university;
    }

    public void setTuwien_university(TUWien_University tuwien_university) {
        this.tuwien_university = tuwien_university;
    }

}