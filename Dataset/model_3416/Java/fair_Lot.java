





import java.util.List;
import java.util.ArrayList;

public class fair_Lot  {

    private String description;
    private String comments;
    private String name;





    private List<fair_Exhibit> fair_exhibits;




    private fair_Exhibit fair_exhibit;


    public fair_Lot(
        String description,        String comments,        String name    ) {
        this.description = description;
        this.comments = comments;
        this.name = name;
        this.fair_exhibits = new ArrayList<>();
    }

    public fair_Lot(
        String description,        String comments,        String name        ArrayList<fair_Exhibit> fair_exhibits    ) {
        this.description = description;
        this.comments = comments;
        this.name = name;
        this.fair_exhibits = fair_exhibits;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<fair_Exhibit> getFair_exhibits() {
        return fair_exhibits;
    }

    public void addFair_exhibit(Fair_exhibit fair_exhibit) {
        this.fair_exhibits.add(fair_exhibit);
    }
    public fair_Exhibit getFair_exhibit() {
        return fair_exhibit;
    }

    public void setFair_exhibit(fair_Exhibit fair_exhibit) {
        this.fair_exhibit = fair_exhibit;
    }

}