





import java.util.List;
import java.util.ArrayList;

public class jsm_AbstractModifiers  {

    private String visibility;
    private boolean synchronized;
    private boolean final;



    public jsm_AbstractModifiers(
        String visibility,        boolean synchronized,        boolean final    ) {
        this.visibility = visibility;
        this.synchronized = synchronized;
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
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }


}