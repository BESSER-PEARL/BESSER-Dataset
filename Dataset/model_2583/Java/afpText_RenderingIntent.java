





import java.util.List;
import java.util.ArrayList;

public class afpText_RenderingIntent extends triplet {

    private String PTOCRI;
    private String IOCARI;
    private String OCRI;
    private String Reserved2;
    private String Reserved;
    private String GOCARI;



    public afpText_RenderingIntent(
        String PTOCRI,        String IOCARI,        String OCRI,        String Reserved2,        String Reserved,        String GOCARI    ) {
        super(
        );
        this.PTOCRI = PTOCRI;
        this.IOCARI = IOCARI;
        this.OCRI = OCRI;
        this.Reserved2 = Reserved2;
        this.Reserved = Reserved;
        this.GOCARI = GOCARI;
    }


    public String getPtocri() {
        return PTOCRI;
    }

    public void setPtocri(String PTOCRI) {
        this.PTOCRI = PTOCRI;
    }
    public String getIocari() {
        return IOCARI;
    }

    public void setIocari(String IOCARI) {
        this.IOCARI = IOCARI;
    }
    public String getOcri() {
        return OCRI;
    }

    public void setOcri(String OCRI) {
        this.OCRI = OCRI;
    }
    public String getReserved2() {
        return Reserved2;
    }

    public void setReserved2(String Reserved2) {
        this.Reserved2 = Reserved2;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getGocari() {
        return GOCARI;
    }

    public void setGocari(String GOCARI) {
        this.GOCARI = GOCARI;
    }


}