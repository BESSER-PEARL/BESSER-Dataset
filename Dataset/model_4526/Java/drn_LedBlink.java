





import java.util.List;
import java.util.ArrayList;

public class drn_LedBlink extends Option {

    private String blink_per_secCST;
    private String color;





    private drn_Parametre drn_parametre;


    public drn_LedBlink(
        String blink_per_secCST,        String color    ) {
        super(
        );
        this.blink_per_secCST = blink_per_secCST;
        this.color = color;
    }


    public String getBlink_per_seccst() {
        return blink_per_secCST;
    }

    public void setBlink_per_seccst(String blink_per_secCST) {
        this.blink_per_secCST = blink_per_secCST;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public drn_Parametre getDrn_parametre() {
        return drn_parametre;
    }

    public void setDrn_parametre(drn_Parametre drn_parametre) {
        this.drn_parametre = drn_parametre;
    }

}