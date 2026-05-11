





import java.util.List;
import java.util.ArrayList;

public class adb_Renaming extends PackageDeclaration {

    private String renamed;



    public adb_Renaming(
        String renamed    ) {
        super(
        );
        this.renamed = renamed;
    }


    public String getRenamed() {
        return renamed;
    }

    public void setRenamed(String renamed) {
        this.renamed = renamed;
    }


}