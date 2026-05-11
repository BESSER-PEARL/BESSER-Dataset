





import java.util.List;
import java.util.ArrayList;

public class afpText_PTD extends structuredField {

    private String YPBASE;
    private String XPBASE;
    private String XPEXTENT;
    private String YPEXTENT;
    private String RESERVED;
    private String XPUNITVL;
    private String YPUNITVL;



    public afpText_PTD(
        String YPBASE,        String XPBASE,        String XPEXTENT,        String YPEXTENT,        String RESERVED,        String XPUNITVL,        String YPUNITVL    ) {
        super(
        );
        this.YPBASE = YPBASE;
        this.XPBASE = XPBASE;
        this.XPEXTENT = XPEXTENT;
        this.YPEXTENT = YPEXTENT;
        this.RESERVED = RESERVED;
        this.XPUNITVL = XPUNITVL;
        this.YPUNITVL = YPUNITVL;
    }


    public String getYpbase() {
        return YPBASE;
    }

    public void setYpbase(String YPBASE) {
        this.YPBASE = YPBASE;
    }
    public String getXpbase() {
        return XPBASE;
    }

    public void setXpbase(String XPBASE) {
        this.XPBASE = XPBASE;
    }
    public String getXpextent() {
        return XPEXTENT;
    }

    public void setXpextent(String XPEXTENT) {
        this.XPEXTENT = XPEXTENT;
    }
    public String getYpextent() {
        return YPEXTENT;
    }

    public void setYpextent(String YPEXTENT) {
        this.YPEXTENT = YPEXTENT;
    }
    public String getReserved() {
        return RESERVED;
    }

    public void setReserved(String RESERVED) {
        this.RESERVED = RESERVED;
    }
    public String getXpunitvl() {
        return XPUNITVL;
    }

    public void setXpunitvl(String XPUNITVL) {
        this.XPUNITVL = XPUNITVL;
    }
    public String getYpunitvl() {
        return YPUNITVL;
    }

    public void setYpunitvl(String YPUNITVL) {
        this.YPUNITVL = YPUNITVL;
    }


}