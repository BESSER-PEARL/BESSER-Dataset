





import java.util.List;
import java.util.ArrayList;

public class requirement_Category extends NamedElement {

    private String id;





    private List<requirement_Category> requirement_categorys;




    private requirement_Repository requirement_repository;




    private requirement_Category requirement_category;




    private requirement_Repository requirement_repository;


    public requirement_Category(
        String id    ) {
        super(
        );
        this.id = id;
        this.requirement_categorys = new ArrayList<>();
    }

    public requirement_Category(
        String id        ArrayList<requirement_Category> requirement_categorys    ) {
        this.id = id;
        this.requirement_categorys = requirement_categorys;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<requirement_Category> getRequirement_categorys() {
        return requirement_categorys;
    }

    public void addRequirement_category(Requirement_category requirement_category) {
        this.requirement_categorys.add(requirement_category);
    }
    public requirement_Repository getRequirement_repository() {
        return requirement_repository;
    }

    public void setRequirement_repository(requirement_Repository requirement_repository) {
        this.requirement_repository = requirement_repository;
    }
    public requirement_Category getRequirement_category() {
        return requirement_category;
    }

    public void setRequirement_category(requirement_Category requirement_category) {
        this.requirement_category = requirement_category;
    }
    public requirement_Repository getRequirement_repository() {
        return requirement_repository;
    }

    public void setRequirement_repository(requirement_Repository requirement_repository) {
        this.requirement_repository = requirement_repository;
    }

}