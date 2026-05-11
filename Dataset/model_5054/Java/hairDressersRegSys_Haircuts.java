





import java.util.List;
import java.util.ArrayList;

public class hairDressersRegSys_Haircuts extends Service {

    private boolean IsCut;
    private boolean IsShave;
    private boolean IsWash;



    public hairDressersRegSys_Haircuts(
        boolean IsCut,        boolean IsShave,        boolean IsWash    ) {
        super(
        );
        this.IsCut = IsCut;
        this.IsShave = IsShave;
        this.IsWash = IsWash;
    }


    public boolean getIscut() {
        return IsCut;
    }

    public void setIscut(boolean IsCut) {
        this.IsCut = IsCut;
    }
    public boolean getIsshave() {
        return IsShave;
    }

    public void setIsshave(boolean IsShave) {
        this.IsShave = IsShave;
    }
    public boolean getIswash() {
        return IsWash;
    }

    public void setIswash(boolean IsWash) {
        this.IsWash = IsWash;
    }


}