





import java.util.List;
import java.util.ArrayList;

public class testcompat103_Thing extends NamedElement {

    private int id;





    private List<testcompat103_RelatedTo> testcompat103_relatedtos;




    private testcompat103_World testcompat103_world;




    private testcompat103_RelatedTo testcompat103_relatedto;




    private testcompat103_RelatedTo testcompat103_relatedto;


    public testcompat103_Thing(
        int id    ) {
        super(
        );
        this.id = id;
        this.testcompat103_relatedtos = new ArrayList<>();
    }

    public testcompat103_Thing(
        int id        ArrayList<testcompat103_RelatedTo> testcompat103_relatedtos    ) {
        this.id = id;
        this.testcompat103_relatedtos = testcompat103_relatedtos;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<testcompat103_RelatedTo> getTestcompat103_relatedtos() {
        return testcompat103_relatedtos;
    }

    public void addTestcompat103_relatedto(Testcompat103_relatedto testcompat103_relatedto) {
        this.testcompat103_relatedtos.add(testcompat103_relatedto);
    }
    public testcompat103_World getTestcompat103_world() {
        return testcompat103_world;
    }

    public void setTestcompat103_world(testcompat103_World testcompat103_world) {
        this.testcompat103_world = testcompat103_world;
    }
    public testcompat103_RelatedTo getTestcompat103_relatedto() {
        return testcompat103_relatedto;
    }

    public void setTestcompat103_relatedto(testcompat103_RelatedTo testcompat103_relatedto) {
        this.testcompat103_relatedto = testcompat103_relatedto;
    }
    public testcompat103_RelatedTo getTestcompat103_relatedto() {
        return testcompat103_relatedto;
    }

    public void setTestcompat103_relatedto(testcompat103_RelatedTo testcompat103_relatedto) {
        this.testcompat103_relatedto = testcompat103_relatedto;
    }

}