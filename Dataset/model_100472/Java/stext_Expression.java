





import java.util.List;
import java.util.ArrayList;

public class stext_Expression extends Statement {






    private stext_EventRaising stext_eventraising;




    private stext_Assignment stext_assignment;


    public stext_Expression(
    ) {
        super(
        );
    }



    public stext_EventRaising getStext_eventraising() {
        return stext_eventraising;
    }

    public void setStext_eventraising(stext_EventRaising stext_eventraising) {
        this.stext_eventraising = stext_eventraising;
    }
    public stext_Assignment getStext_assignment() {
        return stext_assignment;
    }

    public void setStext_assignment(stext_Assignment stext_assignment) {
        this.stext_assignment = stext_assignment;
    }

}