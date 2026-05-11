





import java.util.List;
import java.util.ArrayList;

public class frameweb_DomainAttribute extends Property {

    private String size;
    private boolean isPersistent;
    private boolean isNull;



    public frameweb_DomainAttribute(
        String size,        boolean isPersistent,        boolean isNull    ) {
        super(
        );
        this.size = size;
        this.isPersistent = isPersistent;
        this.isNull = isNull;
    }


    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public boolean getIspersistent() {
        return isPersistent;
    }

    public void setIspersistent(boolean isPersistent) {
        this.isPersistent = isPersistent;
    }
    public boolean getIsnull() {
        return isNull;
    }

    public void setIsnull(boolean isNull) {
        this.isNull = isNull;
    }


}