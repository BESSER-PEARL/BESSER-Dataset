





import java.util.List;
import java.util.ArrayList;

public class simplestatechart_Thing extends NamedElement {

    private int id;





    private simplestatechart_RelatedTo simplestatechart_relatedto;




    private simplestatechart_RelatedTo simplestatechart_relatedto;




    private List<simplestatechart_RelatedTo> simplestatechart_relatedtos;


    public simplestatechart_Thing(
        int id    ) {
        super(
        );
        this.id = id;
        this.simplestatechart_relatedtos = new ArrayList<>();
    }

    public simplestatechart_Thing(
        int id        ArrayList<simplestatechart_RelatedTo> simplestatechart_relatedtos    ) {
        this.id = id;
        this.simplestatechart_relatedtos = simplestatechart_relatedtos;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public simplestatechart_RelatedTo getSimplestatechart_relatedto() {
        return simplestatechart_relatedto;
    }

    public void setSimplestatechart_relatedto(simplestatechart_RelatedTo simplestatechart_relatedto) {
        this.simplestatechart_relatedto = simplestatechart_relatedto;
    }
    public simplestatechart_RelatedTo getSimplestatechart_relatedto() {
        return simplestatechart_relatedto;
    }

    public void setSimplestatechart_relatedto(simplestatechart_RelatedTo simplestatechart_relatedto) {
        this.simplestatechart_relatedto = simplestatechart_relatedto;
    }
    public List<simplestatechart_RelatedTo> getSimplestatechart_relatedtos() {
        return simplestatechart_relatedtos;
    }

    public void addSimplestatechart_relatedto(Simplestatechart_relatedto simplestatechart_relatedto) {
        this.simplestatechart_relatedtos.add(simplestatechart_relatedto);
    }

}