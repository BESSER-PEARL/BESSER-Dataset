





import java.util.List;
import java.util.ArrayList;

public class moba_MobaAuthorization extends MobaApplicationFeature {

    private String name;





    private moba_MobaREST moba_mobarest;


    public moba_MobaAuthorization(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public moba_MobaREST getMoba_mobarest() {
        return moba_mobarest;
    }

    public void setMoba_mobarest(moba_MobaREST moba_mobarest) {
        this.moba_mobarest = moba_mobarest;
    }

}