





import java.util.List;
import java.util.ArrayList;

public class model6_UnorderedList  {






    private List<model6_UnorderedList> model6_unorderedlists;




    private model6_UnorderedList model6_unorderedlist;


    public model6_UnorderedList(
    ) {
        this.model6_unorderedlists = new ArrayList<>();
    }

    public model6_UnorderedList(
        ArrayList<model6_UnorderedList> model6_unorderedlists    ) {
        this.model6_unorderedlists = model6_unorderedlists;
    }


    public List<model6_UnorderedList> getModel6_unorderedlists() {
        return model6_unorderedlists;
    }

    public void addModel6_unorderedlist(Model6_unorderedlist model6_unorderedlist) {
        this.model6_unorderedlists.add(model6_unorderedlist);
    }
    public model6_UnorderedList getModel6_unorderedlist() {
        return model6_unorderedlist;
    }

    public void setModel6_unorderedlist(model6_UnorderedList model6_unorderedlist) {
        this.model6_unorderedlist = model6_unorderedlist;
    }

}