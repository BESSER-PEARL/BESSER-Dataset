





import java.util.List;
import java.util.ArrayList;

public class kreq210_Llll  {

    private String id;





    private kreq210_Gggg kreq210_gggg;




    private kreq210_Hhhh kreq210_hhhh;




    private kreq210_Cccc kreq210_cccc;




    private List<kreq210_Mmmm> kreq210_mmmms;


    public kreq210_Llll(
        String id    ) {
        this.id = id;
        this.kreq210_mmmms = new ArrayList<>();
    }

    public kreq210_Llll(
        String id        ArrayList<kreq210_Mmmm> kreq210_mmmms    ) {
        this.id = id;
        this.kreq210_mmmms = kreq210_mmmms;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public kreq210_Gggg getKreq210_gggg() {
        return kreq210_gggg;
    }

    public void setKreq210_gggg(kreq210_Gggg kreq210_gggg) {
        this.kreq210_gggg = kreq210_gggg;
    }
    public kreq210_Hhhh getKreq210_hhhh() {
        return kreq210_hhhh;
    }

    public void setKreq210_hhhh(kreq210_Hhhh kreq210_hhhh) {
        this.kreq210_hhhh = kreq210_hhhh;
    }
    public kreq210_Cccc getKreq210_cccc() {
        return kreq210_cccc;
    }

    public void setKreq210_cccc(kreq210_Cccc kreq210_cccc) {
        this.kreq210_cccc = kreq210_cccc;
    }
    public List<kreq210_Mmmm> getKreq210_mmmms() {
        return kreq210_mmmms;
    }

    public void addKreq210_mmmm(Kreq210_mmmm kreq210_mmmm) {
        this.kreq210_mmmms.add(kreq210_mmmm);
    }

}