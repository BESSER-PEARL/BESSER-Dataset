





import java.util.List;
import java.util.ArrayList;

public class jsm_AbstractModifiers  {

    private boolean final;
    private String visibility;
    private boolean synchronized;



    public jsm_AbstractModifiers(
        boolean final,        String visibility,        boolean synchronized    ) {
        this.final = final;
        this.visibility = visibility;
        this.synchronized = synchronized;
    }


    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }


}