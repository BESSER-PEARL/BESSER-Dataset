





import java.util.List;
import java.util.ArrayList;

public class build_RepoOption  {

    private String name;





    private build_Repository build_repository;




    private build_BExpression build_bexpression;




    private build_RepositoryUnitProvider build_repositoryunitprovider;


    public build_RepoOption(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public build_Repository getBuild_repository() {
        return build_repository;
    }

    public void setBuild_repository(build_Repository build_repository) {
        this.build_repository = build_repository;
    }
    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }
    public build_RepositoryUnitProvider getBuild_repositoryunitprovider() {
        return build_repositoryunitprovider;
    }

    public void setBuild_repositoryunitprovider(build_RepositoryUnitProvider build_repositoryunitprovider) {
        this.build_repositoryunitprovider = build_repositoryunitprovider;
    }

}