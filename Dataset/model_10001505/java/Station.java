





import java.util.List;
import java.util.ArrayList;

public class Station  {

    private String nameAra;
    private String nameEng;
    private String uid;
    private None location;



    public Station(
        String nameAra,        String nameEng,        String uid,        None location    ) {
        this.nameAra = nameAra;
        this.nameEng = nameEng;
        this.uid = uid;
        this.location = location;
    }


    public String getNameara() {
        return nameAra;
    }

    public void setNameara(String nameAra) {
        this.nameAra = nameAra;
    }
    public String getNameeng() {
        return nameEng;
    }

    public void setNameeng(String nameEng) {
        this.nameEng = nameEng;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public None getLocation() {
        return location;
    }

    public void setLocation(None location) {
        this.location = location;
    }


}