





import java.util.List;
import java.util.ArrayList;

public class Data_Attribut  {

    private String nom;
    private String type;





    private Data_Classe data_classe;


    public Data_Attribut(
        String nom,        String type    ) {
        this.nom = nom;
        this.type = type;
    }


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Data_Classe getData_classe() {
        return data_classe;
    }

    public void setData_classe(Data_Classe data_classe) {
        this.data_classe = data_classe;
    }

}