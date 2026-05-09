





import java.util.List;
import java.util.ArrayList;

public class complworld_Satellite  {

    private String name;





    private complworld_Mars complworld_mars;


    public complworld_Satellite(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public complworld_Mars getComplworld_mars() {
        return complworld_mars;
    }

    public void setComplworld_mars(complworld_Mars complworld_mars) {
        this.complworld_mars = complworld_mars;
    }

}