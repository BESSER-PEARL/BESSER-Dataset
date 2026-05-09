





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Granate extends AbstaktWaffe {

    private String type;
    private String daempfung;



    public shadowrun_Granate(
        String type,        String daempfung    ) {
        super(
        );
        this.type = type;
        this.daempfung = daempfung;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDaempfung() {
        return daempfung;
    }

    public void setDaempfung(String daempfung) {
        this.daempfung = daempfung;
    }


}