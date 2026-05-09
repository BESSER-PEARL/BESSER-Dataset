





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Guidance extends ProcessElement {

    private String text;





    private List<simplepdl_ProcessElement> simplepdl_processelements;


    public simplepdl_Guidance(
        String text    ) {
        super(
        );
        this.text = text;
        this.simplepdl_processelements = new ArrayList<>();
    }

    public simplepdl_Guidance(
        String text        ArrayList<simplepdl_ProcessElement> simplepdl_processelements    ) {
        this.text = text;
        this.simplepdl_processelements = simplepdl_processelements;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public List<simplepdl_ProcessElement> getSimplepdl_processelements() {
        return simplepdl_processelements;
    }

    public void addSimplepdl_processelement(Simplepdl_processelement simplepdl_processelement) {
        this.simplepdl_processelements.add(simplepdl_processelement);
    }

}