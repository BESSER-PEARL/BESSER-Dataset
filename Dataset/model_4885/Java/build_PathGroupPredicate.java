





import java.util.List;
import java.util.ArrayList;

public class build_PathGroupPredicate extends BExpression {






    private build_PathVector build_pathvector;




    private build_BExpression build_bexpression;


    public build_PathGroupPredicate(
    ) {
        super(
        );
    }



    public build_PathVector getBuild_pathvector() {
        return build_pathvector;
    }

    public void setBuild_pathvector(build_PathVector build_pathvector) {
        this.build_pathvector = build_pathvector;
    }
    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }

}