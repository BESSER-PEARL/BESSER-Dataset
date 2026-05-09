





import java.util.List;
import java.util.ArrayList;

public class relationpattern_World extends Category {






    private List<relationpattern_ThingA> relationpattern_thingas;




    private List<relationpattern_RelatedTo> relationpattern_relatedtos;




    private List<relationpattern_ThingB> relationpattern_thingbs;


    public relationpattern_World(
    ) {
        super(
        );
        this.relationpattern_thingas = new ArrayList<>();
        this.relationpattern_relatedtos = new ArrayList<>();
        this.relationpattern_thingbs = new ArrayList<>();
    }

    public relationpattern_World(
        ArrayList<relationpattern_ThingA> relationpattern_thingas,        ArrayList<relationpattern_RelatedTo> relationpattern_relatedtos,        ArrayList<relationpattern_ThingB> relationpattern_thingbs    ) {
        this.relationpattern_thingas = relationpattern_thingas;
        this.relationpattern_relatedtos = relationpattern_relatedtos;
        this.relationpattern_thingbs = relationpattern_thingbs;
    }


    public List<relationpattern_ThingA> getRelationpattern_thingas() {
        return relationpattern_thingas;
    }

    public void addRelationpattern_thinga(Relationpattern_thinga relationpattern_thinga) {
        this.relationpattern_thingas.add(relationpattern_thinga);
    }
    public List<relationpattern_RelatedTo> getRelationpattern_relatedtos() {
        return relationpattern_relatedtos;
    }

    public void addRelationpattern_relatedto(Relationpattern_relatedto relationpattern_relatedto) {
        this.relationpattern_relatedtos.add(relationpattern_relatedto);
    }
    public List<relationpattern_ThingB> getRelationpattern_thingbs() {
        return relationpattern_thingbs;
    }

    public void addRelationpattern_thingb(Relationpattern_thingb relationpattern_thingb) {
        this.relationpattern_thingbs.add(relationpattern_thingb);
    }

}