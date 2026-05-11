





import java.util.List;
import java.util.ArrayList;

public class moba_MobaExternalModule extends MobaApplicationFeature {

    private String name;





    private moba_MobaExternalModule moba_mobaexternalmodule;


    public moba_MobaExternalModule(
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

    public moba_MobaExternalModule getMoba_mobaexternalmodule() {
        return moba_mobaexternalmodule;
    }

    public void setMoba_mobaexternalmodule(moba_MobaExternalModule moba_mobaexternalmodule) {
        this.moba_mobaexternalmodule = moba_mobaexternalmodule;
    }

}