





import java.util.List;
import java.util.ArrayList;

public class documentation_List extends Fragment {






    private List<documentation_ListItem> documentation_listitems;


    public documentation_List(
    ) {
        super(
        );
        this.documentation_listitems = new ArrayList<>();
    }

    public documentation_List(
        ArrayList<documentation_ListItem> documentation_listitems    ) {
        this.documentation_listitems = documentation_listitems;
    }


    public List<documentation_ListItem> getDocumentation_listitems() {
        return documentation_listitems;
    }

    public void addDocumentation_listitem(Documentation_listitem documentation_listitem) {
        this.documentation_listitems.add(documentation_listitem);
    }

}