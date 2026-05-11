





import java.util.List;
import java.util.ArrayList;

public class Maude_Module extends MaudeTopEl {






    private List<Maude_Parameter> maude_parameters;




    private Maude_ModuleIdModExp maude_moduleidmodexp;


    public Maude_Module(
    ) {
        super(
        );
        this.maude_parameters = new ArrayList<>();
    }

    public Maude_Module(
        ArrayList<Maude_Parameter> maude_parameters    ) {
        this.maude_parameters = maude_parameters;
    }


    public List<Maude_Parameter> getMaude_parameters() {
        return maude_parameters;
    }

    public void addMaude_parameter(Maude_parameter maude_parameter) {
        this.maude_parameters.add(maude_parameter);
    }
    public Maude_ModuleIdModExp getMaude_moduleidmodexp() {
        return maude_moduleidmodexp;
    }

    public void setMaude_moduleidmodexp(Maude_ModuleIdModExp maude_moduleidmodexp) {
        this.maude_moduleidmodexp = maude_moduleidmodexp;
    }

}