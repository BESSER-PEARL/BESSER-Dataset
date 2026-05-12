





import java.util.List;
import java.util.ArrayList;

public class build_ConditionalPathVector  {






    private build_BExpression build_bexpression;




    private List<build_PathVector> build_pathvectors;




    private build_BuilderConcernContext build_builderconcerncontext;




    private build_PathGroup build_pathgroup;




    private build_BuilderConcernContext build_builderconcerncontext;


    public build_ConditionalPathVector(
    ) {
        this.build_pathvectors = new ArrayList<>();
    }

    public build_ConditionalPathVector(
        ArrayList<build_PathVector> build_pathvectors    ) {
        this.build_pathvectors = build_pathvectors;
    }


    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }
    public List<build_PathVector> getBuild_pathvectors() {
        return build_pathvectors;
    }

    public void addBuild_pathvector(Build_pathvector build_pathvector) {
        this.build_pathvectors.add(build_pathvector);
    }
    public build_BuilderConcernContext getBuild_builderconcerncontext() {
        return build_builderconcerncontext;
    }

    public void setBuild_builderconcerncontext(build_BuilderConcernContext build_builderconcerncontext) {
        this.build_builderconcerncontext = build_builderconcerncontext;
    }
    public build_PathGroup getBuild_pathgroup() {
        return build_pathgroup;
    }

    public void setBuild_pathgroup(build_PathGroup build_pathgroup) {
        this.build_pathgroup = build_pathgroup;
    }
    public build_BuilderConcernContext getBuild_builderconcerncontext() {
        return build_builderconcerncontext;
    }

    public void setBuild_builderconcerncontext(build_BuilderConcernContext build_builderconcerncontext) {
        this.build_builderconcerncontext = build_builderconcerncontext;
    }

}