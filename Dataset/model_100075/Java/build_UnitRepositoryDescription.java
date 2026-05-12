





import java.util.List;
import java.util.ArrayList;

public class build_UnitRepositoryDescription extends BuildUnitRepository {

    private String evaluatedOptions;





    private build_Repository build_repository;


    public build_UnitRepositoryDescription(
        String evaluatedOptions    ) {
        super(
        );
        this.evaluatedOptions = evaluatedOptions;
    }


    public String getEvaluatedoptions() {
        return evaluatedOptions;
    }

    public void setEvaluatedoptions(String evaluatedOptions) {
        this.evaluatedOptions = evaluatedOptions;
    }

    public build_Repository getBuild_repository() {
        return build_repository;
    }

    public void setBuild_repository(build_Repository build_repository) {
        this.build_repository = build_repository;
    }

}