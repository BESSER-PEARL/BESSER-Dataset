





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String ID;
    private None theme;





    private List<Group> groups;


    public Card(
        String ID,        None theme    ) {
        this.ID = ID;
        this.theme = theme;
        this.groups = new ArrayList<>();
    }

    public Card(
        String ID,        None theme        ArrayList<Group> groups    ) {
        this.ID = ID;
        this.theme = theme;
        this.groups = groups;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public None getTheme() {
        return theme;
    }

    public void setTheme(None theme) {
        this.theme = theme;
    }

    public List<Group> getGroups() {
        return groups;
    }

    public void addGroup(Group group) {
        this.groups.add(group);
    }

}