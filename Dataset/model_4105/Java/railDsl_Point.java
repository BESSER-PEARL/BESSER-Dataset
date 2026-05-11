





import java.util.List;
import java.util.ArrayList;

public class railDsl_Point extends TrackObject {

    private boolean locked;
    private int selectedInput;
    private String kind;
    private int selectedOutput;





    private List<railDsl_Vertex> raildsl_vertexs;




    private List<railDsl_Vertex> raildsl_vertexs;


    public railDsl_Point(
        boolean locked,        int selectedInput,        String kind,        int selectedOutput    ) {
        super(
        );
        this.locked = locked;
        this.selectedInput = selectedInput;
        this.kind = kind;
        this.selectedOutput = selectedOutput;
        this.raildsl_vertexs = new ArrayList<>();
        this.raildsl_vertexs = new ArrayList<>();
    }

    public railDsl_Point(
        boolean locked,        int selectedInput,        String kind,        int selectedOutput        ArrayList<railDsl_Vertex> raildsl_vertexs,        ArrayList<railDsl_Vertex> raildsl_vertexs    ) {
        this.locked = locked;
        this.selectedInput = selectedInput;
        this.kind = kind;
        this.selectedOutput = selectedOutput;
        this.raildsl_vertexs = raildsl_vertexs;
        this.raildsl_vertexs = raildsl_vertexs;
    }

    public boolean getLocked() {
        return locked;
    }

    public void setLocked(boolean locked) {
        this.locked = locked;
    }
    public int getSelectedinput() {
        return selectedInput;
    }

    public void setSelectedinput(int selectedInput) {
        this.selectedInput = selectedInput;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public int getSelectedoutput() {
        return selectedOutput;
    }

    public void setSelectedoutput(int selectedOutput) {
        this.selectedOutput = selectedOutput;
    }

    public List<railDsl_Vertex> getRaildsl_vertexs() {
        return raildsl_vertexs;
    }

    public void addRaildsl_vertex(Raildsl_vertex raildsl_vertex) {
        this.raildsl_vertexs.add(raildsl_vertex);
    }
    public List<railDsl_Vertex> getRaildsl_vertexs() {
        return raildsl_vertexs;
    }

    public void addRaildsl_vertex(Raildsl_vertex raildsl_vertex) {
        this.raildsl_vertexs.add(raildsl_vertex);
    }

}