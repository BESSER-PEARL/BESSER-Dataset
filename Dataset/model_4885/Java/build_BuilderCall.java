





import java.util.List;
import java.util.ArrayList;

public class build_BuilderCall extends BuilderInput {

    private String builderName;



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


}