





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private String name;





    private List<Beitrag> beitrags;




    private Benutzer benutzer;


    public Group(
        String name    ) {
        this.name = name;
        this.beitrags = new ArrayList<>();
    }

    public Group(
        String name        ArrayList<Beitrag> beitrags    ) {
        this.name = name;
        this.beitrags = beitrags;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Beitrag> getBeitrags() {
        return beitrags;
    }

    public void addBeitrag(Beitrag beitrag) {
        this.beitrags.add(beitrag);
    }
    public Benutzer getBenutzer() {
        return benutzer;
    }

    public void setBenutzer(Benutzer benutzer) {
        this.benutzer = benutzer;
    }

}