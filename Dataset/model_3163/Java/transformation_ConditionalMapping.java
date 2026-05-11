





import java.util.List;
import java.util.ArrayList;

public class transformation_ConditionalMapping extends ContentMapping {






    private transformation_OtherwiseClause transformation_otherwiseclause;




    private List<transformation_WhenClause> transformation_whenclauses;


    public transformation_ConditionalMapping(
    ) {
        super(
        );
        this.transformation_whenclauses = new ArrayList<>();
    }

    public transformation_ConditionalMapping(
        ArrayList<transformation_WhenClause> transformation_whenclauses    ) {
        this.transformation_whenclauses = transformation_whenclauses;
    }


    public transformation_OtherwiseClause getTransformation_otherwiseclause() {
        return transformation_otherwiseclause;
    }

    public void setTransformation_otherwiseclause(transformation_OtherwiseClause transformation_otherwiseclause) {
        this.transformation_otherwiseclause = transformation_otherwiseclause;
    }
    public List<transformation_WhenClause> getTransformation_whenclauses() {
        return transformation_whenclauses;
    }

    public void addTransformation_whenclause(Transformation_whenclause transformation_whenclause) {
        this.transformation_whenclauses.add(transformation_whenclause);
    }

}