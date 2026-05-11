





import java.util.List;
import java.util.ArrayList;

public class kmLogo_Block extends Instruction {






    private kmLogo_While kmlogo_while;




    private kmLogo_Repeat kmlogo_repeat;


    public kmLogo_Block(
    ) {
        super(
        );
    }



    public kmLogo_While getKmlogo_while() {
        return kmlogo_while;
    }

    public void setKmlogo_while(kmLogo_While kmlogo_while) {
        this.kmlogo_while = kmlogo_while;
    }
    public kmLogo_Repeat getKmlogo_repeat() {
        return kmlogo_repeat;
    }

    public void setKmlogo_repeat(kmLogo_Repeat kmlogo_repeat) {
        this.kmlogo_repeat = kmlogo_repeat;
    }

}