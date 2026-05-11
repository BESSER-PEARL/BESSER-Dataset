





import java.util.List;
import java.util.ArrayList;

public class pokerleague_IdentifiableEntity extends Serializable {

    private boolean proxy;
    private int id;
    private boolean obsolete;



    public pokerleague_IdentifiableEntity(
        boolean proxy,        int id,        boolean obsolete    ) {
        super(
        );
        this.proxy = proxy;
        this.id = id;
        this.obsolete = obsolete;
    }


    public boolean getProxy() {
        return proxy;
    }

    public void setProxy(boolean proxy) {
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


}