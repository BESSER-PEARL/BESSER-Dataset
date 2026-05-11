





import java.util.List;
import java.util.ArrayList;

public class sihuhu_Switch extends TrackElement {






    private List<sihuhu_Rail> sihuhu_rails;




    private sihuhu_Track sihuhu_track;


    public sihuhu_Switch(
    ) {
        super(
        );
        this.sihuhu_rails = new ArrayList<>();
    }

    public sihuhu_Switch(
        ArrayList<sihuhu_Rail> sihuhu_rails    ) {
        this.sihuhu_rails = sihuhu_rails;
    }


    public List<sihuhu_Rail> getSihuhu_rails() {
        return sihuhu_rails;
    }

    public void addSihuhu_rail(Sihuhu_rail sihuhu_rail) {
        this.sihuhu_rails.add(sihuhu_rail);
    }
    public sihuhu_Track getSihuhu_track() {
        return sihuhu_track;
    }

    public void setSihuhu_track(sihuhu_Track sihuhu_track) {
        this.sihuhu_track = sihuhu_track;
    }

}