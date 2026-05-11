





import java.util.List;
import java.util.ArrayList;

public class model_AbstractMClassFieldDeclaration extends AbstractMFieldDeclaration {

    private boolean final;
    private String visibility;



    public model_AbstractMClassFieldDeclaration(
        boolean final,        String visibility    ) {
        super(
        );
        this.final = final;
        this.visibility = visibility;
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


}