





import java.util.List;
import java.util.ArrayList;

public class Maude_Parameter extends ModExpression {

    private String label;





    private Maude_Module maude_module;


    public Maude_Parameter(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public Maude_Module getMaude_module() {
        return maude_module;
    }

    public void setMaude_module(Maude_Module maude_module) {
        this.maude_module = maude_module;
    }

}