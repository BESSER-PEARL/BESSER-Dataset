





import java.util.List;
import java.util.ArrayList;

public class siddhi_OutputEventType extends RAW, ALL, EXPIRED, CURRENT, EVENTS {






    private siddhi_DefinitionWindow siddhi_definitionwindow;


    public siddhi_OutputEventType(
    ) {
        super(
        );
    }



    public siddhi_DefinitionWindow getSiddhi_definitionwindow() {
        return siddhi_definitionwindow;
    }

    public void setSiddhi_definitionwindow(siddhi_DefinitionWindow siddhi_definitionwindow) {
        this.siddhi_definitionwindow = siddhi_definitionwindow;
    }

}