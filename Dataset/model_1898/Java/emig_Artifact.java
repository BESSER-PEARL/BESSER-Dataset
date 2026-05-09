





import java.util.List;
import java.util.ArrayList;

public class emig_Artifact extends LocatedElement {

    private String type;





    private emig_MigrationProgram emig_migrationprogram;


    public emig_Artifact(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public emig_MigrationProgram getEmig_migrationprogram() {
        return emig_migrationprogram;
    }

    public void setEmig_migrationprogram(emig_MigrationProgram emig_migrationprogram) {
        this.emig_migrationprogram = emig_migrationprogram;
    }

}