





import java.util.List;
import java.util.ArrayList;

public class moba_MobaTrigger extends MobaApplicationFeature {

    private String name;





    private moba_MobaTrigger moba_mobatrigger;


    public moba_MobaTrigger(
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

    public moba_MobaTrigger getMoba_mobatrigger() {
        return moba_mobatrigger;
    }

    public void setMoba_mobatrigger(moba_MobaTrigger moba_mobatrigger) {
        this.moba_mobatrigger = moba_mobatrigger;
    }

}