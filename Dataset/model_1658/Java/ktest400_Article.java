





import java.util.List;
import java.util.ArrayList;

public class ktest400_Article extends NamedElement {

    private String aid;





    private ktest400_World ktest400_world;


    public ktest400_Article(
        String aid    ) {
        super(
        );
        this.aid = aid;
    }


    public String getAid() {
        return aid;
    }

    public void setAid(String aid) {
        this.aid = aid;
    }

    public ktest400_World getKtest400_world() {
        return ktest400_world;
    }

    public void setKtest400_world(ktest400_World ktest400_world) {
        this.ktest400_world = ktest400_world;
    }

}