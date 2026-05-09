





import java.util.List;
import java.util.ArrayList;

public class pDL1_Guidance extends ProcessElement {

    private String texte;



    public pDL1_Guidance(
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