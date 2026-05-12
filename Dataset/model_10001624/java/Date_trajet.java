





import java.util.List;
import java.util.ArrayList;

public class Date_trajet  {

    private int id_date;
    private String Date___heure__minute;
    private String Jour;
    private String Type_date;



    public Date_trajet(
        int id_date,        String Date___heure__minute,        String Jour,        String Type_date    ) {
        this.id_date = id_date;
        this.Date___heure__minute = Date___heure__minute;
        this.Jour = Jour;
        this.Type_date = Type_date;
    }


    public int getId_date() {
        return id_date;
    }

    public void setId_date(int id_date) {
        this.id_date = id_date;
    }
    public String getDate___heure__minute() {
        return Date___heure__minute;
    }

    public void setDate___heure__minute(String Date___heure__minute) {
        this.Date___heure__minute = Date___heure__minute;
    }
    public String getJour() {
        return Jour;
    }

    public void setJour(String Jour) {
        this.Jour = Jour;
    }
    public String getType_date() {
        return Type_date;
    }

    public void setType_date(String Type_date) {
        this.Type_date = Type_date;
    }


}