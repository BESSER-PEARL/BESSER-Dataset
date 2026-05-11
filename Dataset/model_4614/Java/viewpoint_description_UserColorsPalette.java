





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_UserColorsPalette  {

    private String name;





    private List<UserColor> usercolors;


    public viewpoint_description_UserColorsPalette(
        String name    ) {
        this.name = name;
        this.usercolors = new ArrayList<>();
    }

    public viewpoint_description_UserColorsPalette(
        String name        ArrayList<UserColor> usercolors    ) {
        this.name = name;
        this.usercolors = usercolors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<UserColor> getUsercolors() {
        return usercolors;
    }

    public void addUsercolor(Usercolor usercolor) {
        this.usercolors.add(usercolor);
    }

}