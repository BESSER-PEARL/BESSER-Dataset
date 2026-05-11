





import java.util.List;
import java.util.ArrayList;

public class fair_Lot  {

    private String description;
    private String name;
    private String comments;





    private fair_Exhibit fair_exhibit;




    private List<fair_Exhibit> fair_exhibits;


    public fair_Lot(
        String description,        String name,        String comments    ) {
        this.description = description;
        this.name = name;
        this.comments = comments;
        this.fair_exhibits = new ArrayList<>();
    }

    public fair_Lot(
        String description,        String name,        String comments        ArrayList<fair_Exhibit> fair_exhibits    ) {
        this.description = description;
        this.name = name;
        this.comments = comments;
        this.fair_exhibits = fair_exhibits;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }

    public fair_Exhibit getFair_exhibit() {
        return fair_exhibit;
    }

    public void setFair_exhibit(fair_Exhibit fair_exhibit) {
        this.fair_exhibit = fair_exhibit;
    }
    public List<fair_Exhibit> getFair_exhibits() {
        return fair_exhibits;
    }

    public void addFair_exhibit(Fair_exhibit fair_exhibit) {
        this.fair_exhibits.add(fair_exhibit);
    }

}