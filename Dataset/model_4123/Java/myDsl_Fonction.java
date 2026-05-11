





import java.util.List;
import java.util.ArrayList;

public class myDsl_Fonction  {

    private String nom;





    private myDsl_Program mydsl_program;


    public myDsl_Fonction(
        String nom    ) {
        this.nom = nom;
    }


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public myDsl_Program getMydsl_program() {
        return mydsl_program;
    }

    public void setMydsl_program(myDsl_Program mydsl_program) {
        this.mydsl_program = mydsl_program;
    }

}