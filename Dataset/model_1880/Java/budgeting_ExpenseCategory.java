





import java.util.List;
import java.util.ArrayList;

public class budgeting_ExpenseCategory extends Category {

    private String patterns;



    public budgeting_ExpenseCategory(
        String patterns    ) {
        super(
        );
        this.patterns = patterns;
    }


    public String getPatterns() {
        return patterns;
    }

    public void setPatterns(String patterns) {
        this.patterns = patterns;
    }


}