





import java.util.List;
import java.util.ArrayList;

public class frameweb_DomainAttribute extends Property {

    private String size;
    private boolean isNull;
    private boolean isPersistent;



    public frameweb_DomainAttribute(
        String size,        boolean isNull,        boolean isPersistent    ) {
        super(
        );
        this.size = size;
        this.isNull = isNull;
        this.isPersistent = isPersistent;
    }


    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public boolean getIsnull() {
        return isNull;
    }

    public void setIsnull(boolean isNull) {
        this.isNull = isNull;
    }
    public boolean getIspersistent() {
        return isPersistent;
    }

    public void setIspersistent(boolean isPersistent) {
        this.isPersistent = isPersistent;
    }


}