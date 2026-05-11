





import java.util.List;
import java.util.ArrayList;

public class caltrop_InputPattern extends PortPattern, ActionPattern {

    private String variables;





    private caltrop_FireAction caltrop_fireaction;


    public caltrop_InputPattern(
        String variables    ) {
        super(
        );
        this.variables = variables;
    }


    public String getVariables() {
        return variables;
    }

    public void setVariables(String variables) {
        this.variables = variables;
    }

    public caltrop_FireAction getCaltrop_fireaction() {
        return caltrop_fireaction;
    }

    public void setCaltrop_fireaction(caltrop_FireAction caltrop_fireaction) {
        this.caltrop_fireaction = caltrop_fireaction;
    }

}