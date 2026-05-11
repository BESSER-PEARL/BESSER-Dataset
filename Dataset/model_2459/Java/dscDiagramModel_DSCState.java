





import java.util.List;
import java.util.ArrayList;

public class dscDiagramModel_DSCState extends Container {

    private String Variables;
    private boolean isSimple;



    public dscDiagramModel_DSCState(
        String Variables,        boolean isSimple    ) {
        super(
        );
        this.Variables = Variables;
        this.isSimple = isSimple;
    }


    public String getVariables() {
        return Variables;
    }

    public void setVariables(String Variables) {
        this.Variables = Variables;
    }
    public boolean getIssimple() {
        return isSimple;
    }

    public void setIssimple(boolean isSimple) {
        this.isSimple = isSimple;
    }


}