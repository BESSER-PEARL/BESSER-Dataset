





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_SistedesMember extends Person {






    private List<sistedesMM_Edition> sistedesmm_editions;


    public sistedesMM_SistedesMember(
    ) {
        super(
        );
        this.sistedesmm_editions = new ArrayList<>();
    }

    public sistedesMM_SistedesMember(
        ArrayList<sistedesMM_Edition> sistedesmm_editions    ) {
        this.sistedesmm_editions = sistedesmm_editions;
    }


    public List<sistedesMM_Edition> getSistedesmm_editions() {
        return sistedesmm_editions;
    }

    public void addSistedesmm_edition(Sistedesmm_edition sistedesmm_edition) {
        this.sistedesmm_editions.add(sistedesmm_edition);
    }

}