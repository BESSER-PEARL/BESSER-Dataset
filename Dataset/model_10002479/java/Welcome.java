





import java.util.List;
import java.util.ArrayList;

public class Welcome  {

    private String personal;
    private String placements;
    private String academic;



    public Welcome(
        String personal,        String placements,        String academic    ) {
        this.personal = personal;
        this.placements = placements;
        this.academic = academic;
    }


    public String getPersonal() {
        return personal;
    }

    public void setPersonal(String personal) {
        this.personal = personal;
    }
    public String getPlacements() {
        return placements;
    }

    public void setPlacements(String placements) {
        this.placements = placements;
    }
    public String getAcademic() {
        return academic;
    }

    public void setAcademic(String academic) {
        this.academic = academic;
    }


}