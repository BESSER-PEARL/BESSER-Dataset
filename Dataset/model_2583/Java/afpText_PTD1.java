





import java.util.List;
import java.util.ArrayList;

public class afpText_PTD1 extends structuredField {

    private String XPEXTENT;
    private String RESERVED;
    private String YPEXTENT;
    private String XPBASE;
    private String YPBASE;
    private String XPUNITVL;
    private String YPUNITVL;



    public afpText_PTD1(
        String XPEXTENT,        String RESERVED,        String YPEXTENT,        String XPBASE,        String YPBASE,        String XPUNITVL,        String YPUNITVL    ) {
        super(
        );
        this.XPEXTENT = XPEXTENT;
        this.RESERVED = RESERVED;
        this.YPEXTENT = YPEXTENT;
        this.XPBASE = XPBASE;
        this.YPBASE = YPBASE;
        this.XPUNITVL = XPUNITVL;
        this.YPUNITVL = YPUNITVL;
    }


    public String getXpextent() {
        return XPEXTENT;
    }

    public void setXpextent(String XPEXTENT) {
        this.XPEXTENT = XPEXTENT;
    }
    public String getReserved() {
        return RESERVED;
    }

    public void setReserved(String RESERVED) {
        this.RESERVED = RESERVED;
    }
    public String getYpextent() {
        return YPEXTENT;
    }

    public void setYpextent(String YPEXTENT) {
        this.YPEXTENT = YPEXTENT;
    }
    public String getXpbase() {
        return XPBASE;
    }

    public void setXpbase(String XPBASE) {
        this.XPBASE = XPBASE;
    }
    public String getYpbase() {
        return YPBASE;
    }

    public void setYpbase(String YPBASE) {
        this.YPBASE = YPBASE;
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