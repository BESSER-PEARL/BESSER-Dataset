





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETTypeModifiers  {

    private boolean const;
    private boolean urgent;
    private boolean meta;





    private ecdarText_ETType ecdartext_ettype;


    public ecdarText_ETTypeModifiers(
        boolean const,        boolean urgent,        boolean meta    ) {
        this.const = const;
        this.urgent = urgent;
        this.meta = meta;
    }


    public boolean getConst() {
        return const;
    }

    public void setConst(boolean const) {
        this.const = const;
    }
    public boolean getUrgent() {
        return urgent;
    }

    public void setUrgent(boolean urgent) {
        this.urgent = urgent;
    }
    public boolean getMeta() {
        return meta;
    }

    public void setMeta(boolean meta) {
        this.meta = meta;
    }

    public ecdarText_ETType getEcdartext_ettype() {
        return ecdartext_ettype;
    }

    public void setEcdartext_ettype(ecdarText_ETType ecdartext_ettype) {
        this.ecdartext_ettype = ecdartext_ettype;
    }

}