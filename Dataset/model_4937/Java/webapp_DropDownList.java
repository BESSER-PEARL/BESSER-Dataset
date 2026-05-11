





import java.util.List;
import java.util.ArrayList;

public class webapp_DropDownList extends Control {






    private List<webapp_ListElement> webapp_listelements;


    public webapp_DropDownList(
    ) {
        super(
        );
        this.webapp_listelements = new ArrayList<>();
    }

    public webapp_DropDownList(
        ArrayList<webapp_ListElement> webapp_listelements    ) {
        this.webapp_listelements = webapp_listelements;
    }


    public List<webapp_ListElement> getWebapp_listelements() {
        return webapp_listelements;
    }

    public void addWebapp_listelement(Webapp_listelement webapp_listelement) {
        this.webapp_listelements.add(webapp_listelement);
    }

}