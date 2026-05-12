





import java.util.List;
import java.util.ArrayList;

public class WELCOME_PAGE  {

    private String academic;
    private String placements;
    private String personal;



    public WELCOME_PAGE(
        String academic,        String placements,        String personal    ) {
        this.academic = academic;
        this.placements = placements;
        this.personal = personal;
    }


    public String getAcademic() {
        return academic;
    }

    public void setAcademic(String academic) {
        this.academic = academic;
    }
    public String getPlacements() {
        return placements;
    }

    public void setPlacements(String placements) {
        this.placements = placements;
    }
    public String getPersonal() {
        return personal;
    }

    public void setPersonal(String personal) {
        this.personal = personal;
    }


}