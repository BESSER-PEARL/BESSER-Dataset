





import java.util.List;
import java.util.ArrayList;

public class kmLogo_VarDecl extends Instruction {

    private String key;





    private kmLogo_LogoProgram kmlogo_logoprogram;


    public kmLogo_VarDecl(
        String key    ) {
        super(
        );
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public kmLogo_LogoProgram getKmlogo_logoprogram() {
        return kmlogo_logoprogram;
    }

    public void setKmlogo_logoprogram(kmLogo_LogoProgram kmlogo_logoprogram) {
        this.kmlogo_logoprogram = kmlogo_logoprogram;
    }

}