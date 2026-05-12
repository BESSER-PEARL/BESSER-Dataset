





import java.util.List;
import java.util.ArrayList;

public class cours  {

    private String heureF;
    private String dateCours;
    private int id;
    private String heureD;



    public cours(
        String heureF,        String dateCours,        int id,        String heureD    ) {
        this.heureF = heureF;
        this.dateCours = dateCours;
        this.id = id;
        this.heureD = heureD;
    }


    public String getHeuref() {
        return heureF;
    }

    public void setHeuref(String heureF) {
        this.heureF = heureF;
    }
    public String getDatecours() {
        return dateCours;
    }

    public void setDatecours(String dateCours) {
        this.dateCours = dateCours;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getHeured() {
        return heureD;
    }

    public void setHeured(String heureD) {
        this.heureD = heureD;
    }


}