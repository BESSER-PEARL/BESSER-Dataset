





import java.util.List;
import java.util.ArrayList;

public class model_AbstractModifiers  {

    private String visibility;
    private boolean final;
    private boolean synchronized;



    public model_AbstractModifiers(
        String visibility,        boolean final,        boolean synchronized    ) {
        this.visibility = visibility;
        this.final = final;
        this.synchronized = synchronized;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }


}