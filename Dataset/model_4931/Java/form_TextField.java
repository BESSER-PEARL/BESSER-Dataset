





import java.util.List;
import java.util.ArrayList;

public class form_TextField extends InputField {

    private boolean encrypted;



    public form_TextField(
        boolean encrypted    ) {
        super(
        );
        this.encrypted = encrypted;
    }


    public boolean getEncrypted() {
        return encrypted;
    }

    public void setEncrypted(boolean encrypted) {
        this.encrypted = encrypted;
    }


}