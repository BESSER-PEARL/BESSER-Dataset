





import java.util.List;
import java.util.ArrayList;

public class build_BuilderCall extends BuilderInput {

    private String builderName;





    private build_BuilderCallFacade build_buildercallfacade;


    public build_BuilderCall(
        String builderName    ) {
        super(
        );
        this.builderName = builderName;
    }


    public String getBuildername() {
        return builderName;
    }

    public void setBuildername(String builderName) {
        this.builderName = builderName;
    }

    public build_BuilderCallFacade getBuild_buildercallfacade() {
        return build_buildercallfacade;
    }

    public void setBuild_buildercallfacade(build_BuilderCallFacade build_buildercallfacade) {
        this.build_buildercallfacade = build_buildercallfacade;
    }

}