





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Guidance extends ProcessElements {

    private String text;





    private simplepdl_ProcessElements simplepdl_processelements;


    public simplepdl_Guidance(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public simplepdl_ProcessElements getSimplepdl_processelements() {
        return simplepdl_processelements;
    }

    public void setSimplepdl_processelements(simplepdl_ProcessElements simplepdl_processelements) {
        this.simplepdl_processelements = simplepdl_processelements;
    }

}