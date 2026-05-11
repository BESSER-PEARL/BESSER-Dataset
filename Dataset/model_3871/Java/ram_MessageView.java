





import java.util.List;
import java.util.ArrayList;

public class ram_MessageView extends AbstractMessageView {






    private ram_Interaction ram_interaction;




    private ram_Operation ram_operation;


    public ram_MessageView(
    ) {
        super(
        );
    }



    public ram_Interaction getRam_interaction() {
        return ram_interaction;
    }

    public void setRam_interaction(ram_Interaction ram_interaction) {
        this.ram_interaction = ram_interaction;
    }
    public ram_Operation getRam_operation() {
        return ram_operation;
    }

    public void setRam_operation(ram_Operation ram_operation) {
        this.ram_operation = ram_operation;
    }

}