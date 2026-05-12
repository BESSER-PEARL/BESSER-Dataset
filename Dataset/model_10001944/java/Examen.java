





import java.util.List;
import java.util.ArrayList;

public class Examen  {

    private int id;
    private String heureF;
    private String typeExamen;
    private String heureD;
    private String dateExamen;



    public Examen(
        int id,        String heureF,        String typeExamen,        String heureD,        String dateExamen    ) {
        this.id = id;
        this.heureF = heureF;
        this.typeExamen = typeExamen;
        this.heureD = heureD;
        this.dateExamen = dateExamen;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getHeuref() {
        return heureF;
    }

    public void setHeuref(String heureF) {
        this.heureF = heureF;
    }
    public String getTypeexamen() {
        return typeExamen;
    }

    public void setTypeexamen(String typeExamen) {
        this.typeExamen = typeExamen;
    }
    public String getHeured() {
        return heureD;
    }

    public void setHeured(String heureD) {
        this.heureD = heureD;
    }
    public String getDateexamen() {
        return dateExamen;
    }

    public void setDateexamen(String dateExamen) {
        this.dateExamen = dateExamen;
    }


}