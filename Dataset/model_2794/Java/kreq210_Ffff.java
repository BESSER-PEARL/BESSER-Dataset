





import java.util.List;
import java.util.ArrayList;

public class kreq210_Ffff  {

    private String id;





    private kreq210_Cccc kreq210_cccc;




    private List<kreq210_Ffff> kreq210_ffffs;


    public kreq210_Ffff(
        String id    ) {
        this.id = id;
        this.kreq210_ffffs = new ArrayList<>();
    }

    public kreq210_Ffff(
        String id        ArrayList<kreq210_Ffff> kreq210_ffffs    ) {
        this.id = id;
        this.kreq210_ffffs = kreq210_ffffs;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public kreq210_Cccc getKreq210_cccc() {
        return kreq210_cccc;
    }

    public void setKreq210_cccc(kreq210_Cccc kreq210_cccc) {
        this.kreq210_cccc = kreq210_cccc;
    }
    public List<kreq210_Ffff> getKreq210_ffffs() {
        return kreq210_ffffs;
    }

    public void addKreq210_ffff(Kreq210_ffff kreq210_ffff) {
        this.kreq210_ffffs.add(kreq210_ffff);
    }

}