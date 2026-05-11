





import java.util.List;
import java.util.ArrayList;

public class solution_EntityPage extends DynamicPage {






    private List<solution_DynamicPage> solution_dynamicpages;


    public solution_EntityPage(
    ) {
        super(
        );
        this.solution_dynamicpages = new ArrayList<>();
    }

    public solution_EntityPage(
        ArrayList<solution_DynamicPage> solution_dynamicpages    ) {
        this.solution_dynamicpages = solution_dynamicpages;
    }


    public List<solution_DynamicPage> getSolution_dynamicpages() {
        return solution_dynamicpages;
    }

    public void addSolution_dynamicpage(Solution_dynamicpage solution_dynamicpage) {
        this.solution_dynamicpages.add(solution_dynamicpage);
    }

}