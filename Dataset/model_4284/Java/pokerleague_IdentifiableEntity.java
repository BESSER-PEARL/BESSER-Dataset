





import java.util.List;
import java.util.ArrayList;

public class pokerleague_IdentifiableEntity extends Serializable {

    private boolean obsolete;
    private int id;
    private boolean proxy;



    public pokerleague_IdentifiableEntity(
        boolean obsolete,        int id,        boolean proxy    ) {
        super(
        );
        this.obsolete = obsolete;
        this.id = id;
        this.proxy = proxy;
    }


    public boolean getObsolete() {
        return obsolete;
    }

    public void setObsolete(boolean obsolete) {
        this.obsolete = obsolete;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public boolean getProxy() {
        return proxy;
    }

    public void setProxy(boolean proxy) {
        this.proxy = proxy;
    }


}