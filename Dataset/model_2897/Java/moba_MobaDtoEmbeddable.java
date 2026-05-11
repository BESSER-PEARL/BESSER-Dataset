





import java.util.List;
import java.util.ArrayList;

public class moba_MobaDtoEmbeddable extends MobaDtoFeature, MobaMultiplicityAble {

    private String alias;
    private boolean transient;





    private moba_MobaDto moba_mobadto;


    public moba_MobaDtoEmbeddable(
        String alias,        boolean transient    ) {
        super(
        );
        this.alias = alias;
        this.transient = transient;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }

    public moba_MobaDto getMoba_mobadto() {
        return moba_mobadto;
    }

    public void setMoba_mobadto(moba_MobaDto moba_mobadto) {
        this.moba_mobadto = moba_mobadto;
    }

}