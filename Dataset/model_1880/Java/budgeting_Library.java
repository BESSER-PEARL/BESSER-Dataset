





import java.util.List;
import java.util.ArrayList;

public class budgeting_Library extends BudgetingFile {

    private String name;





    private List<budgeting_Category> budgeting_categorys;


    public budgeting_Library(
        String name    ) {
        super(
        );
        this.name = name;
        this.budgeting_categorys = new ArrayList<>();
    }

    public budgeting_Library(
        String name        ArrayList<budgeting_Category> budgeting_categorys    ) {
        this.name = name;
        this.budgeting_categorys = budgeting_categorys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<budgeting_Category> getBudgeting_categorys() {
        return budgeting_categorys;
    }

    public void addBudgeting_category(Budgeting_category budgeting_category) {
        this.budgeting_categorys.add(budgeting_category);
    }

}