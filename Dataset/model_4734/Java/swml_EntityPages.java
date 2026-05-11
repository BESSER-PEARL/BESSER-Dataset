





import java.util.List;
import java.util.ArrayList;

public class swml_EntityPages extends dynamicPage {






    private List<swml_dynamicPage> swml_dynamicpages;


    public swml_EntityPages(
    ) {
        super(
        );
        this.swml_dynamicpages = new ArrayList<>();
    }

    public swml_EntityPages(
        ArrayList<swml_dynamicPage> swml_dynamicpages    ) {
        this.swml_dynamicpages = swml_dynamicpages;
    }


    public List<swml_dynamicPage> getSwml_dynamicpages() {
        return swml_dynamicpages;
    }

    public void addSwml_dynamicpage(Swml_dynamicpage swml_dynamicpage) {
        this.swml_dynamicpages.add(swml_dynamicpage);
    }

}