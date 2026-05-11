





import java.util.List;
import java.util.ArrayList;

public class moba_MobaGenerator extends MobaApplicationFeature {

    private String name;
    private boolean active;





    private moba_MobaGeneratorMixinFeature moba_mobageneratormixinfeature;


    public moba_MobaGenerator(
        String name,        boolean active    ) {
        super(
        );
        this.name = name;
        this.active = active;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public moba_MobaGeneratorMixinFeature getMoba_mobageneratormixinfeature() {
        return moba_mobageneratormixinfeature;
    }

    public void setMoba_mobageneratormixinfeature(moba_MobaGeneratorMixinFeature moba_mobageneratormixinfeature) {
        this.moba_mobageneratormixinfeature = moba_mobageneratormixinfeature;
    }

}