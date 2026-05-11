





import java.util.List;
import java.util.ArrayList;

public class di_Connector extends View {

    private String target;
    private String source;





    private List<di_Bendpoint> di_bendpoints;


    public di_Connector(
        String target,        String source    ) {
        super(
        );
        this.target = target;
        this.source = source;
        this.di_bendpoints = new ArrayList<>();
    }

    public di_Connector(
        String target,        String source        ArrayList<di_Bendpoint> di_bendpoints    ) {
        this.target = target;
        this.source = source;
        this.di_bendpoints = di_bendpoints;
    }

    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public List<di_Bendpoint> getDi_bendpoints() {
        return di_bendpoints;
    }

    public void addDi_bendpoint(Di_bendpoint di_bendpoint) {
        this.di_bendpoints.add(di_bendpoint);
    }

}