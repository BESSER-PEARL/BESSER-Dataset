





import java.util.List;
import java.util.ArrayList;

public class relationworld_World extends Category {






    private List<relationworld_RelatedTo> relationworld_relatedtos;




    private List<relationworld_ThingA> relationworld_thingas;




    private List<relationworld_ThingB> relationworld_thingbs;


    public relationworld_World(
    ) {
        super(
        );
        this.relationworld_relatedtos = new ArrayList<>();
        this.relationworld_thingas = new ArrayList<>();
        this.relationworld_thingbs = new ArrayList<>();
    }

    public relationworld_World(
        ArrayList<relationworld_RelatedTo> relationworld_relatedtos,        ArrayList<relationworld_ThingA> relationworld_thingas,        ArrayList<relationworld_ThingB> relationworld_thingbs    ) {
        this.relationworld_relatedtos = relationworld_relatedtos;
        this.relationworld_thingas = relationworld_thingas;
        this.relationworld_thingbs = relationworld_thingbs;
    }


    public List<relationworld_RelatedTo> getRelationworld_relatedtos() {
        return relationworld_relatedtos;
    }

    public void addRelationworld_relatedto(Relationworld_relatedto relationworld_relatedto) {
        this.relationworld_relatedtos.add(relationworld_relatedto);
    }
    public List<relationworld_ThingA> getRelationworld_thingas() {
        return relationworld_thingas;
    }

    public void addRelationworld_thinga(Relationworld_thinga relationworld_thinga) {
        this.relationworld_thingas.add(relationworld_thinga);
    }
    public List<relationworld_ThingB> getRelationworld_thingbs() {
        return relationworld_thingbs;
    }

    public void addRelationworld_thingb(Relationworld_thingb relationworld_thingb) {
        this.relationworld_thingbs.add(relationworld_thingb);
    }

}