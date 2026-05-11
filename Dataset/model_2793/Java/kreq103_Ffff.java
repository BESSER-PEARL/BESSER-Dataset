





import java.util.List;
import java.util.ArrayList;

public class kreq103_Ffff  {

    private String id;





    private kreq103_Cccc kreq103_cccc;




    private List<kreq103_Ffff> kreq103_ffffs;


    public kreq103_Ffff(
        String id    ) {
        this.id = id;
        this.kreq103_ffffs = new ArrayList<>();
    }

    public kreq103_Ffff(
        String id        ArrayList<kreq103_Ffff> kreq103_ffffs    ) {
        this.id = id;
        this.kreq103_ffffs = kreq103_ffffs;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public kreq103_Cccc getKreq103_cccc() {
        return kreq103_cccc;
    }

    public void setKreq103_cccc(kreq103_Cccc kreq103_cccc) {
        this.kreq103_cccc = kreq103_cccc;
    }
    public List<kreq103_Ffff> getKreq103_ffffs() {
        return kreq103_ffffs;
    }

    public void addKreq103_ffff(Kreq103_ffff kreq103_ffff) {
        this.kreq103_ffffs.add(kreq103_ffff);
    }

}