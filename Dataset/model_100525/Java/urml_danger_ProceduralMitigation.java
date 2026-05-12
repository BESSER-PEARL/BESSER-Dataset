





import java.util.List;
import java.util.ArrayList;

public class urml_danger_ProceduralMitigation extends Mitigation {

    private String mitigationProcedure;



    public urml_danger_ProceduralMitigation(
        String mitigationProcedure    ) {
        super(
        );
        this.mitigationProcedure = mitigationProcedure;
    }


    public String getMitigationprocedure() {
        return mitigationProcedure;
    }

    public void setMitigationprocedure(String mitigationProcedure) {
        this.mitigationProcedure = mitigationProcedure;
    }


}