





import java.util.List;
import java.util.ArrayList;

public class model_PetriNet extends HasLabel, HasToolInfo, HasId, HasName {

    private String type;





    private List<model_Page> model_pages;




    private model_Page model_page;


    public model_PetriNet(
        String type    ) {
        super(
        );
        this.type = type;
        this.model_pages = new ArrayList<>();
    }

    public model_PetriNet(
        String type        ArrayList<model_Page> model_pages    ) {
        this.type = type;
        this.model_pages = model_pages;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<model_Page> getModel_pages() {
        return model_pages;
    }

    public void addModel_page(Model_page model_page) {
        this.model_pages.add(model_page);
    }
    public model_Page getModel_page() {
        return model_page;
    }

    public void setModel_page(model_Page model_page) {
        this.model_page = model_page;
    }

}