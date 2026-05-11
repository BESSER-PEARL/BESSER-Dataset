





import java.util.List;
import java.util.ArrayList;

public class nabla_Function extends FunctionOrReduction {

    private boolean external;





    private nabla_NablaModule nabla_nablamodule;


    public nabla_Function(
        boolean external    ) {
        super(
        );
        this.external = external;
    }


    public boolean getExternal() {
        return external;
    }

    public void setExternal(boolean external) {
        this.external = external;
    }

    public nabla_NablaModule getNabla_nablamodule() {
        return nabla_nablamodule;
    }

    public void setNabla_nablamodule(nabla_NablaModule nabla_nablamodule) {
        this.nabla_nablamodule = nabla_nablamodule;
    }

}