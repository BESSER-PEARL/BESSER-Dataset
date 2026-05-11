





import java.util.List;
import java.util.ArrayList;

public class lobj_Precognition  {

    private String id;
    private String precog;





    private lobj_DidacMeta lobj_didacmeta;


    public lobj_Precognition(
        String id,        String precog    ) {
        this.id = id;
        this.precog = precog;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPrecog() {
        return precog;
    }

    public void setPrecog(String precog) {
        this.precog = precog;
    }

    public lobj_DidacMeta getLobj_didacmeta() {
        return lobj_didacmeta;
    }

    public void setLobj_didacmeta(lobj_DidacMeta lobj_didacmeta) {
        this.lobj_didacmeta = lobj_didacmeta;
    }

}