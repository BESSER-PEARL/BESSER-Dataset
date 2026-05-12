





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private String name;
    private String discription;



    public Group(
        String name,        String discription    ) {
        this.name = name;
        this.discription = discription;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDiscription() {
        return discription;
    }

    public void setDiscription(String discription) {
        this.discription = discription;
    }


}