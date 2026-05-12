





import java.util.List;
import java.util.ArrayList;

public class Draw_Path  {

    private String Name;
    private String Route;



    public Draw_Path(
        String Name,        String Route    ) {
        this.Name = Name;
        this.Route = Route;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getRoute() {
        return Route;
    }

    public void setRoute(String Route) {
        this.Route = Route;
    }


}