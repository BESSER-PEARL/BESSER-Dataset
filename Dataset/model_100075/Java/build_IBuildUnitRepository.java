





import java.util.List;
import java.util.ArrayList;

public class build_IBuildUnitRepository  {






    private build_RepositoryUnitProvider build_repositoryunitprovider;




    private build_CompoundBuildUnitRepository build_compoundbuildunitrepository;




    private build_Repository build_repository;


    public build_IBuildUnitRepository(
    ) {
    }



    public build_RepositoryUnitProvider getBuild_repositoryunitprovider() {
        return build_repositoryunitprovider;
    }

    public void setBuild_repositoryunitprovider(build_RepositoryUnitProvider build_repositoryunitprovider) {
        this.build_repositoryunitprovider = build_repositoryunitprovider;
    }
    public build_CompoundBuildUnitRepository getBuild_compoundbuildunitrepository() {
        return build_compoundbuildunitrepository;
    }

    public void setBuild_compoundbuildunitrepository(build_CompoundBuildUnitRepository build_compoundbuildunitrepository) {
        this.build_compoundbuildunitrepository = build_compoundbuildunitrepository;
    }
    public build_Repository getBuild_repository() {
        return build_repository;
    }

    public void setBuild_repository(build_Repository build_repository) {
        this.build_repository = build_repository;
    }

}