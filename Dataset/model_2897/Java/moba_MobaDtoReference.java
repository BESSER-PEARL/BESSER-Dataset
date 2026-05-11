





import java.util.List;
import java.util.ArrayList;

public class moba_MobaDtoReference extends MobaDtoFeature, MobaMultiplicityAble {

    private boolean lazy;
    private String alias;
    private boolean cascading;
    private boolean transient;





    private moba_MobaDtoReference moba_mobadtoreference;




    private moba_MobaDto moba_mobadto;


    public moba_MobaDtoReference(
        boolean lazy,        String alias,        boolean cascading,        boolean transient    ) {
        super(
        );
        this.lazy = lazy;
        this.alias = alias;
        this.cascading = cascading;
        this.transient = transient;
    }


    public boolean getLazy() {
        return lazy;
    }

    public void setLazy(boolean lazy) {
        this.lazy = lazy;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public boolean getCascading() {
        return cascading;
    }

    public void setCascading(boolean cascading) {
        this.cascading = cascading;
    }
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }

    public moba_MobaDtoReference getMoba_mobadtoreference() {
        return moba_mobadtoreference;
    }

    public void setMoba_mobadtoreference(moba_MobaDtoReference moba_mobadtoreference) {
        this.moba_mobadtoreference = moba_mobadtoreference;
    }
    public moba_MobaDto getMoba_mobadto() {
        return moba_mobadto;
    }

    public void setMoba_mobadto(moba_MobaDto moba_mobadto) {
        this.moba_mobadto = moba_mobadto;
    }

}