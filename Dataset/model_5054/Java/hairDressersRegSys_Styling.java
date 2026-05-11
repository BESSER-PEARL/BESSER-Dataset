





import java.util.List;
import java.util.ArrayList;

public class hairDressersRegSys_Styling extends Service {

    private boolean IsWash;



    public hairDressersRegSys_Styling(
        boolean IsWash    ) {
        super(
        );
        this.IsWash = IsWash;
    }


    public boolean getIswash() {
        return IsWash;
    }

    public void setIswash(boolean IsWash) {
        this.IsWash = IsWash;
    }


}