





import java.util.List;
import java.util.ArrayList;

public class pDL2_Guidance extends ProcessElement {

    private String texte;



    public pDL2_Guidance(
        String texte    ) {
        super(
        );
        this.texte = texte;
    }


    public String getTexte() {
        return texte;
    }

    public void setTexte(String texte) {
        this.texte = texte;
    }


}