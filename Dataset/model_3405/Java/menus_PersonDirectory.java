





import java.util.List;
import java.util.ArrayList;

public class menus_PersonDirectory  {






    private List<menus_Person> menus_persons;


    public menus_PersonDirectory(
    ) {
        this.menus_persons = new ArrayList<>();
    }

    public menus_PersonDirectory(
        ArrayList<menus_Person> menus_persons    ) {
        this.menus_persons = menus_persons;
    }


    public List<menus_Person> getMenus_persons() {
        return menus_persons;
    }

    public void addMenus_person(Menus_person menus_person) {
        this.menus_persons.add(menus_person);
    }

}