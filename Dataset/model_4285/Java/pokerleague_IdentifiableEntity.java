





import java.util.List;
import java.util.ArrayList;

public class pokerleague_IdentifiableEntity extends Serializable {

    private int id;
    private boolean obsolete;
    private boolean proxy;



    public pokerleague_IdentifiableEntity(
        int id,        boolean obsolete,        boolean proxy    ) {
        super(
        );
        this.id = id;
        this.obsolete = obsolete;
        this.proxy = proxy;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public boolean getObsolete() {
        return obsolete;
    }

    public void setObsolete(boolean obsolete) {
        this.obsolete = obsolete;
    }
    public boolean getProxy() {
        return proxy;
    }

    public void setProxy(boolean proxy) {
        this.proxy = proxy;
    }


}