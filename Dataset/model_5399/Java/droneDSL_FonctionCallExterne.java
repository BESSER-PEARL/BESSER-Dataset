





import java.util.List;
import java.util.ArrayList;

public class droneDSL_FonctionCallExterne extends FonctionCall {

    private String name;





    private droneDSL_Import dronedsl_import;


    public droneDSL_FonctionCallExterne(
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

    public droneDSL_Import getDronedsl_import() {
        return dronedsl_import;
    }

    public void setDronedsl_import(droneDSL_Import dronedsl_import) {
        this.dronedsl_import = dronedsl_import;
    }

}