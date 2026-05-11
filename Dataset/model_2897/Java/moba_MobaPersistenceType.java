





import java.util.List;
import java.util.ArrayList;

public class moba_MobaPersistenceType extends MobaApplicationFeature {

    private String name;





    private moba_MobaCache moba_mobacache;


    public moba_MobaPersistenceType(
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

    public moba_MobaCache getMoba_mobacache() {
        return moba_mobacache;
    }

    public void setMoba_mobacache(moba_MobaCache moba_mobacache) {
        this.moba_mobacache = moba_mobacache;
    }

}