





import java.util.List;
import java.util.ArrayList;

public class connection_SubscriberTable extends TdTable {

    private boolean system;





    private connection_CDCType connection_cdctype;


    public connection_SubscriberTable(
        boolean system    ) {
        super(
        );
        this.system = system;
    }


    public boolean getSystem() {
        return system;
    }

    public void setSystem(boolean system) {
        this.system = system;
    }

    public connection_CDCType getConnection_cdctype() {
        return connection_cdctype;
    }

    public void setConnection_cdctype(connection_CDCType connection_cdctype) {
        this.connection_cdctype = connection_cdctype;
    }

}