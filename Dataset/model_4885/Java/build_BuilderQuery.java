





import java.util.List;
import java.util.ArrayList;

public class build_BuilderQuery  {






    private List<build_BExpression> build_bexpressions;




    private build_BExpression build_bexpression;




    private build_Synchronization build_synchronization;


    public build_BuilderQuery(
    ) {
        this.build_bexpressions = new ArrayList<>();
    }

    public build_BuilderQuery(
        ArrayList<build_BExpression> build_bexpressions    ) {
        this.build_bexpressions = build_bexpressions;
    }


    public List<build_BExpression> getBuild_bexpressions() {
        return build_bexpressions;
    }

    public void addBuild_bexpression(Build_bexpression build_bexpression) {
        this.build_bexpressions.add(build_bexpression);
    }
    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }
    public build_Synchronization getBuild_synchronization() {
        return build_synchronization;
    }

    public void setBuild_synchronization(build_Synchronization build_synchronization) {
        this.build_synchronization = build_synchronization;
    }

}