





import java.util.List;
import java.util.ArrayList;

public class emig_Rule extends LocatedElement {

    private String name;





    private emig_MigrationLibrary emig_migrationlibrary;




    private emig_MigrationProgram emig_migrationprogram;


    public emig_Rule(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public emig_MigrationLibrary getEmig_migrationlibrary() {
        return emig_migrationlibrary;
    }

    public void setEmig_migrationlibrary(emig_MigrationLibrary emig_migrationlibrary) {
        this.emig_migrationlibrary = emig_migrationlibrary;
    }
    public emig_MigrationProgram getEmig_migrationprogram() {
        return emig_migrationprogram;
    }

    public void setEmig_migrationprogram(emig_MigrationProgram emig_migrationprogram) {
        this.emig_migrationprogram = emig_migrationprogram;
    }

}