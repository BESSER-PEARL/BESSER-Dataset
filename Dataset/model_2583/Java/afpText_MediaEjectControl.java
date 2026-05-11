





import java.util.List;
import java.util.ArrayList;

public class afpText_MediaEjectControl extends triplet {

    private String EjCtrl;
    private String Reserved;



    public afpText_MediaEjectControl(
        String EjCtrl,        String Reserved    ) {
        super(
        );
        this.EjCtrl = EjCtrl;
        this.Reserved = Reserved;
    }


    public String getEjctrl() {
        return EjCtrl;
    }

    public void setEjctrl(String EjCtrl) {
        this.EjCtrl = EjCtrl;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }


}