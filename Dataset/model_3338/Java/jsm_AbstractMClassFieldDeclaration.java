





import java.util.List;
import java.util.ArrayList;

public class jsm_AbstractMClassFieldDeclaration extends AbstractMFieldDeclaration {

    private String visibility;
    private boolean final;



    public jsm_AbstractMClassFieldDeclaration(
        String visibility,        boolean final    ) {
        super(
        );
        this.visibility = visibility;
        this.final = final;
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


}